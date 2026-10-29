"""
Задание 5. Анализатор учебных результатов.
"""

students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}


def mean(values: list[float]) -> float:
    if not values:
        return 0.0
    total = 0.0
    for v in values:
        total += v
    return total / len(values)


def minimum(values: list[float]) -> float:
    if not values:
        return 0.0
    best = values[0]
    for v in values[1:]:
        if v < best:
            best = v
    return best


def maximum(values: list[float]) -> float:
    if not values:
        return 0.0
    best = values[0]
    for v in values[1:]:
        if v > best:
            best = v
    return best


def classify(score: float) -> str:
    if score >= 90:
        return "отлично"
    if score >= 75:
        return "хорошо"
    if score >= 60:
        return "удовлетворительно"
    return "неудовлетворительно"


def student_summary(name: str, results: list[int]) -> dict:
    if not results:
        return {
            "имя": name,
            "среднее": 0.0,
            "минимум": 0.0,
            "максимум": 0.0,
            "категория": "нет данных",
            "количество": 0,
        }
    avg = mean(results)
    return {
        "имя": name,
        "среднее": avg,
        "минимум": minimum(results),
        "максимум": maximum(results),
        "категория": classify(avg),
        "количество": len(results),
    }


def group_summary(students: dict) -> dict:
    summaries = [student_summary(n, r) for n, r in students.items()]

    valid = [s["среднее"] for s in summaries if s["количество"] > 0]

    categories = {"отлично": 0, "хорошо": 0, "удовлетворительно": 0, "неудовлетворительно": 0, "нет данных": 0}
    for s in summaries:
        categories[s["категория"]] += 1
    return {
        "количество студентов": len(students),
        "среднее группы": mean(valid),
        "категории": categories,
        "summaries": summaries,
    }


def find_top_students(students: dict) -> list[str]:
    if not students:
        return []
    best = None
    for results in students.values():
        if not results:
            continue
        avg = mean(results)
        if best is None or avg > best:
            best = avg
    if best is None:
        return []
    return [n for n, r in students.items() if r and mean(r) == best]

def format_report(student_data: dict, group_data: dict) -> str:
    lines = ["=" * 40, "ОТЧЁТ ПО ГРУППЕ", "=" * 40]

    for s in group_data["summaries"]:
        lines.append(
            f"{s['имя']}: среднее={s['среднее']:.2f}, "
            f"мин={s['минимум']}, макс={s['максимум']}, "
            f"категория={s['категория']}"
        )

    lines += [
        "-" * 40,
        f"Всего студентов: {group_data['количество студентов']}",
        f"Среднее группы: {group_data['среднее группы']:.2f}",
        "Категории:",
    ]
    lines += [f"  {cat}: {cnt}" for cat, cnt in group_data["категории"].items() if cnt]

    tops = find_top_students(student_data)
    lines.append(f"Лидер(ы): {', '.join(tops) if tops else 'нет данных'}")

    return "\n".join(lines)


print(">>> Сценарий 1: обычный набор")
print(format_report(students, group_summary(students)))

print("\n>>> Сценарий 2: один студент")
one = {"Анна": [90, 95]}
print(format_report(one, group_summary(one)))

print("\n>>> Сценарий 3: несколько лидеров")
multi = {"А": [80, 90], "Б": [85, 85], "В": [70, 70]}
print(format_report(multi, group_summary(multi)))

print("\n>>> Сценарий 4: пустая группа")
empty = {}
print(format_report(empty, group_summary(empty)))

print("\n>>> Сценарий 5: студент без результатов")
mixed = {"Анна": [90], "Борис": []}
print(format_report(mixed, group_summary(mixed)))

print("\n>>> Сценарий 6: границы категорий")
ranges = {"Анна": [59.9, 60], "Борис": [74.9, 89.9]}
print(format_report(ranges, group_summary(ranges)))

