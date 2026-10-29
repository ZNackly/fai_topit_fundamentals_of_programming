def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""
    return sum(values) / len(values)


def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит каждую часть имени к нужному регистру."""
    if not name or not name.strip():
        return ""
    parts = name.split()
    correct = ""
    for part in parts:
        correct = correct.join(part.capitalize())
    return correct


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Формирует строковый отчет о результатах студента."""
    if not results:
        return f"{prefix} для {student}: нет данных"
    avg = arithmetic_mean([float(r) for r in results])
    return f"{prefix} для {student}: среднее = {avg:.{precision}f} (n={len(results)})"


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""
    seen: list[str] = []
    for tag in tags:
        cleaned = tag.strip()
        if not cleaned:
            continue
        if lowercase:
            cleaned = cleaned.lower()
        if cleaned not in seen:
            seen.append(cleaned)
    return tuple(seen)



assert arithmetic_mean([2.0, 4.0, 6.0]) == 4.0
assert arithmetic_mean([10]) == 10.0
assert arithmetic_mean([]) == 0.0

assert normalize_name("  ivan   petrov ") == "Ivan Petrov"
assert normalize_name("ANNA") == "Anna"
assert normalize_name("   ") == ""

assert build_report("Ivan", [5, 4, 3]) == "Результат для Ivan: среднее = 4.00 (n=3)"
assert build_report("Ivan", []) == "Результат для Ivan: нет данных"
assert build_report("Ivan", [2, 2], precision=0, prefix="Итог") == "Итог для Ivan: среднее = 2 (n=2)"

assert collect_tags(" A ", "b", "A", "") == ("a", "b")
assert collect_tags("X", "x", lowercase=False) == ("X", "x")
assert collect_tags() == ()

print("Все проверки пройдены.")



print("среднее:", arithmetic_mean([1, 2, 3]))
print("среднее по имени:", arithmetic_mean(values=[4, 5]))

print("имя:", normalize_name("  oleg  "))
print("имя по имени:", normalize_name(name="  oleg  "))

print(build_report("Ivan", [5, 4, 3]))
print(build_report("Ivan", [5, 4, 3], precision=1, prefix="Средний балл"))

print("теги:", collect_tags(" A ", "b", "A", "", lowercase=True))
print("теги по имени:", collect_tags("X", "y", lowercase=False))



scores = [5, 4, 3, 5]
print("среднее через *:", arithmetic_mean(*scores))

kwargs = {"precision": 1, "prefix": "Балл"}
print("отчёт через **:", build_report("Maria", [5, 5, 4], **kwargs))

tag_list = [" Misha ", "Sasha", "Anya", ""]
print("теги через *:", collect_tags(*tag_list))

course = "Python"


def outer():
    course = "Вложенный курс"

    def inner():
        nonlocal course
        course = "Изменённый курс"
        return course

    print("outer до вызова inner:  ", course)
    result = inner()
    print("outer после вызова inner:", course)
    print("inner вернул:            ", result)
    return course


print("глобальный course до:  ", course)
outer_result = outer()
print("outer вернул:          ", outer_result)
print("глобальный course после:", course)

def add_result_broken(value, results=[]):
    results.append(value)
    return results


def add_result_fixed(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results



print("--- ошибочная версия ---")
print(add_result_broken(1))
print(add_result_broken(2))
print(add_result_broken(3))

print("--- исправленная версия ---")
print(add_result_fixed(1))
print(add_result_fixed(2))
print(add_result_fixed(3))

shared = [0]
print(add_result_fixed(9, shared))


def apply_to_results(operation, values):
    """Применяет функцию к каждому значению и возвращает новый список."""
    return [operation(v) for v in values]


def make_threshold_checker(threshold: int):
    def checker(result: int) -> bool:
        return result >= threshold
    return checker



values = [3, 5, 7, 9]

def double(x: int) -> int:
    return x * 2

print("именованная double:", apply_to_results(double, values))
print("lambda квадрат:", apply_to_results(lambda x: x * x, values))

pass_3 = make_threshold_checker(3)
pass_5 = make_threshold_checker(5)

pass_3(4)
pass_5(4)
print(f"Порог 3: {pass_3(4)} \n Порог 5: {pass_5(4)}")