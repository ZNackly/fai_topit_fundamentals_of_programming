from abc import ABC, abstractmethod
from datetime import datetime
from typing import Callable, Iterator, overload

from task_4 import Course, Student, Submission


class CourseEvent(ABC):

    def __init__(self) -> None:
        self.created_at: datetime = datetime.now()

    @property
    @abstractmethod
    def student_id(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def describe(self) -> str:
        raise NotImplementedError


class SubmissionEvent(CourseEvent):
    def __init__(self, submission: Submission) -> None:
        super().__init__()
        self.submission = submission

    @property
    def student_id(self) -> str:
        return self.submission.student_id

    @property
    def score(self) -> float:
        return self.submission.score

    def describe(self) -> str:
        s = self.submission
        return (
            f"{s.student_id} сдал {s.laboratory_id} "
            f"(попытка {s.attempt}), результат {s.score}"
        )


class AttendanceEvent(CourseEvent):
    def __init__(self, student_id: str, lesson: str, present: bool = True) -> None:
        super().__init__()
        self._student_id = student_id
        self.lesson = lesson
        self.present = present

    @property
    def student_id(self) -> str:
        return self._student_id

    def describe(self) -> str:
        status = "присутствовал" if self.present else "отсутствовал"
        return f"{self.student_id} {status} на занятии «{self.lesson}»"


class CommentEvent(CourseEvent):
    def __init__(self, student_id: str, text: str) -> None:
        super().__init__()
        self._student_id = student_id
        self.text = text

    @property
    def student_id(self) -> str:
        return self._student_id

    def describe(self) -> str:
        return f"Комментарий для {self.student_id}: {self.text}"


class DeadlineEvent(CourseEvent):
    def __init__(self, student_id: str, laboratory_id: str, deadline: str) -> None:
        super().__init__()
        self._student_id = student_id
        self.laboratory_id = laboratory_id
        self.deadline = deadline

    @property
    def student_id(self) -> str:
        return self._student_id

    def describe(self) -> str:
        return f"{self.student_id}: срок сдачи {self.laboratory_id} — {self.deadline}"


class CourseJournal:

    def __init__(self) -> None:
        self._events: list[CourseEvent] = []

    def add(self, event: CourseEvent) -> None:
        if not isinstance(event, CourseEvent):
            raise TypeError("В журнал можно добавлять только CourseEvent")
        self._events.append(event)

    def events_for_student(self, student_id: str) -> Iterator[CourseEvent]:
        for event in self._events:
            if event.student_id == student_id:
                yield event

    def events_by_type(self, event_type: type[CourseEvent]) -> Iterator[CourseEvent]:
        for event in self._events:
            if isinstance(event, event_type):
                yield event

    def summary(self) -> dict[str, object]:
        by_type: dict[str, int] = {}
        for event in self._events:
            name = type(event).__name__
            by_type[name] = by_type.get(name, 0) + 1
        return {"total": len(self._events), "by_type": by_type}

    def __len__(self) -> int:
        return len(self._events)

    def __iter__(self) -> Iterator[CourseEvent]:
        return iter(self._events)

    @overload
    def __getitem__(self, index: int) -> CourseEvent:
        return self._events[index]

    @overload
    def __getitem__(self, index: slice) -> list[CourseEvent]:
        return self._events[index]

    def __getitem__(self, index: int | slice) -> CourseEvent | list[CourseEvent]:
        return self._events[index]

    def __str__(self) -> str:
        return f"Журнал: {len(self)} событий"

    def __repr__(self) -> str:
        return f"CourseJournal(events={len(self)})"


def render_timeline(events: Iterator[CourseEvent] | list[CourseEvent] | CourseJournal) -> str:
    return "\n".join(
        f"{event.created_at:%H:%M:%S} | {event.describe()}"
        for event in events
    )


class ScoreView:

    def __init__(self, journal: CourseJournal) -> None:
        self._journal = journal

    def __iter__(self) -> Iterator[float]:
        for event in self._journal:
            if isinstance(event, SubmissionEvent):
                yield event.score


class FilteredJournalView:

    def __init__(
        self,
        journal: CourseJournal,
        predicate: Callable[[CourseEvent], bool],
    ) -> None:
        self._journal = journal
        self._predicate = predicate

    def __iter__(self) -> Iterator[CourseEvent]:
        for event in self._journal:
            if self._predicate(event):
                yield event


def is_comment(event: CourseEvent) -> bool:
    return isinstance(event, CommentEvent)


if __name__ == "__main__":
    course = Course()
    course.add_student(Student("s1", "Иван Петров"))
    course.add_student(Student("s2", "Анна Смирнова"))
    course.add_student(Student("s3", "Олег Орлов"))

    journal = CourseJournal()
    journal.add(AttendanceEvent("s1", "Лекция 1"))
    journal.add(AttendanceEvent("s2", "Лекция 1"))
    journal.add(AttendanceEvent("s3", "Лекция 1", present=False))
    journal.add(SubmissionEvent(course.submit("s1", "lab1", 1, 60)))
    journal.add(CommentEvent("s1", "Добавьте проверку входных данных"))
    journal.add(SubmissionEvent(course.submit("s1", "lab1", 2, 85)))
    journal.add(SubmissionEvent(course.submit("s2", "lab1", 1, 95)))
    journal.add(CommentEvent("s2", "Отличная работа"))
    journal.add(SubmissionEvent(course.submit("s3", "lab1", 1, 40)))
    journal.add(AttendanceEvent("s2", "Лекция 2"))

    print(journal)
    print(repr(journal))
    print("len(journal) =", len(journal))

    print("--- События студента s1 ---")
    for event in journal.events_for_student("s1"):
        print(event.describe())

    print("--- События типа SubmissionEvent ---")
    for event in journal.events_by_type(SubmissionEvent):
        print(event.describe())

    print("--- Индекс и срез ---")
    print(journal[0].describe())
    print([event.describe() for event in journal[3:5]])

    print("--- Временная шкала ---")
    print(render_timeline(journal))

    print("--- Сводка ---")
    print(journal.summary())

    print("--- ScoreView ---")
    scores = ScoreView(journal)
    score_values = list(scores)
    print("результаты:", score_values)
    print("повторный обход:", list(scores))
    print(
        "количество:", len(score_values),
        "; максимум:", max(score_values),
        "; минимум:", min(score_values),
        "; среднее:", sum(score_values) / len(score_values),
    )

    print("--- DeadlineEvent: render_timeline не менялась ---")
    journal.add(DeadlineEvent("s3", "lab2", "2026-12-01"))
    print(render_timeline(journal[-2:]))

    print("--- FilteredJournalView ---")
    comments = FilteredJournalView(journal, is_comment)
    print("именованная функция:", [event.describe() for event in comments])
    print("повторный обход:", len(list(comments)))

    s2_events = FilteredJournalView(
        journal, lambda event: event.student_id == "s2"
    )
    print("lambda (студент s2):", len(list(s2_events)))
    print("повторный обход:", len(list(s2_events)))
