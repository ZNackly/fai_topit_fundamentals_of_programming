from dataclasses import dataclass


@dataclass
class Submission:
    student_id: str
    laboratory_id: str
    attempt: int
    score: float
    comment: str = ""

    def __post_init__(self) -> None:
        if not self.student_id or not self.laboratory_id:
            raise ValueError("Идентификаторы не должны быть пустыми")
        if self.attempt < 1:
            raise ValueError("Номер попытки должен быть положительным")
        if not 0 <= self.score <= 100:
            raise ValueError("Результат должен быть от 0 до 100")


class Student:

    def __init__(self, student_id: str, name: str) -> None:
        if not Student.is_valid_student_id(student_id):
            raise ValueError("Некорректный идентификатор студента")
        self.student_id = student_id
        self.name = name
        self._submissions: list[Submission] = []

    @classmethod
    def from_full_name(cls, student_id: str, full_name: str) -> "Student":
        return cls(student_id, " ".join(full_name.split()))

    @staticmethod
    def is_valid_student_id(student_id: str) -> bool:
        return isinstance(student_id, str) and student_id.strip() != ""

    def add_submission(self, submission: Submission) -> None:
        if submission.student_id != self.student_id:
            raise ValueError("Работа принадлежит другому студенту")
        self._submissions.append(submission)

    @property
    def submissions(self) -> tuple[Submission, ...]:
        return tuple(self._submissions)

    @property
    def average_score(self) -> float:
        if not self._submissions:
            return 0.0
        return sum(s.score for s in self._submissions) / len(self._submissions)

    def best_score(self, laboratory_id: str):
        scores = [s.score for s in self._submissions if s.laboratory_id == laboratory_id]
        if not scores:
            return None
        return max(scores)

    def sorted_submissions(self) -> list[Submission]:
        return sorted(self._submissions, key=lambda s: (s.attempt, s.score))

    def __len__(self) -> int:
        return len(self._submissions)

    def __iter__(self):
        return iter(self._submissions)

    def __str__(self) -> str:
        return f"{self.name} ({self.student_id}): попыток {len(self)}, средний балл {self.average_score:.1f}"

    def __repr__(self) -> str:
        return f"Student(student_id={self.student_id!r}, name={self.name!r}, submissions={len(self)})"


class Course:


    def __init__(self) -> None:
        self._students: dict[str, Student] = {}

    def add_student(self, student: Student) -> None:
        if student.student_id in self._students:
            raise ValueError("Студент уже зарегистрирован")
        self._students[student.student_id] = student

    def get_student(self, student_id: str) -> Student:
        return self._students[student_id]

    def submit(self, student_id: str, laboratory_id: str, attempt: int, score: float, comment: str = "") -> Submission:
        submission = Submission(student_id, laboratory_id, attempt, score, comment)
        self.get_student(student_id).add_submission(submission)
        return submission

    def top_students(self, limit: int = 3) -> list[Student]:
        ordered = sorted(self._students.values(), key=lambda s: s.average_score, reverse=True)
        return ordered[:limit]

    def __contains__(self, student_id: str) -> bool:
        return student_id in self._students

    def __len__(self) -> int:
        return len(self._students)

    def __iter__(self):
        return iter(self._students.values())


if __name__ == "__main__":
    course = Course()
    course.add_student(Student("s1", "Иван Петров"))
    course.add_student(Student.from_full_name("s2", "  Анна   Смирнова "))
    course.add_student(Student("s3", "Олег Орлов"))

    course.submit("s1", "lab1", 1, 60)
    course.submit("s1", "lab1", 2, 85, "после доработки")
    course.submit("s1", "lab2", 1, 70)
    course.submit("s2", "lab1", 1, 95)
    course.submit("s3", "lab1", 1, 40)

    ivan = course.get_student("s1")
    print(ivan)
    print(repr(ivan))
    print("len(ivan) =", len(ivan))
    print("средний балл:", ivan.average_score)
    print("лучший по lab1:", ivan.best_score("lab1"), "; по lab9:", ivan.best_score("lab9"))
    print("итерация по работам:")
    for submission in ivan:
        print("  ", submission)

    print("--- submissions отдает копию ---")
    copy = ivan.submissions
    print(type(copy).__name__, len(copy))
    try:
        copy.append(None)
    except AttributeError as error:
        print("Изменить нельзя:", error)

    print("--- сортировка не меняет исходный порядок ---")
    print([(s.laboratory_id, s.attempt, s.score) for s in ivan.sorted_submissions()])
    print([(s.laboratory_id, s.attempt, s.score) for s in ivan])

    print("--- сравнение по содержимому ---")
    print(Submission("s1", "lab1", 1, 60) == Submission("s1", "lab1", 1, 60))
    print(Submission("s1", "lab1", 1, 60) == Submission("s1", "lab1", 2, 60))

    print("--- Course ---")
    print("len(course) =", len(course))
    print("'s1' in course:", "s1" in course, "; 's9' in course:", "s9" in course)
    print("студенты:", [s.name for s in course])
    print("топ-2:", [s.name for s in course.top_students(2)])
    print("iter(course):", iter(course))
    print("is_valid_student_id:", Student.is_valid_student_id("s1"), Student.is_valid_student_id("  "))

    print("--- проверка инвариантов ---")
    for args in [("", "lab1", 1, 50), ("s1", "lab1", 0, 50), ("s1", "lab1", 1, 101)]:
        try:
            Submission(*args)
        except ValueError as error:
            print(args, "->", error)