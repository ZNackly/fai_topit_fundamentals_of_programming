import sys
import tracemalloc
from collections import deque


def read_measurements(lines):
    for line in lines:
        line = line.strip()
        if line:
            yield float(line)


def filter_range(values, minimum: float, maximum: float):
    for value in values:
        if minimum <= value <= maximum:
            yield value


def moving_average(values, window_size: int):
    if window_size < 1:
        raise ValueError("Размер окна должен быть положительным")
    window = deque(maxlen=window_size)
    for value in values:
        window.append(value)
        if len(window) == window_size:
            yield sum(window) / window_size


def take(n: int, iterable):
    if n <= 0:
        return
    count = 0
    for item in iterable:
        yield item
        count += 1
        if count == n:
            return


def drop(n: int, iterable):
    skipped = 0
    for item in iterable:
        if skipped < n:
            skipped += 1
        else:
            yield item


def batch(iterable, size: int):
    if size < 1:
        raise ValueError("Размер пакета должен быть положительным")
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def lazy_run(n: int) -> float:
    lines = (str(i % 100) for i in range(n))
    total = 0.0
    for average in moving_average(filter_range(read_measurements(lines), 10, 90), 5):
        total += average
    return total


def list_run(n: int) -> float:
    lines = [str(i % 100) for i in range(n)]
    numbers = [float(line) for line in lines]
    filtered = [x for x in numbers if 10 <= x <= 90]
    averages = []
    for i in range(len(filtered) - 4):
        averages.append(sum(filtered[i:i + 5]) / 5)
    total = 0.0
    for average in averages:
        total += average
    return total


def peak_memory_kb(function, n: int):
    tracemalloc.start()
    result = function(n)
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return result, peak / 1024


if __name__ == "__main__":
    raw_lines = ["10.0", "", "12.5", "100.0", "11.5", "13.0", "9.5"]

    def build_pipeline():
        return moving_average(filter_range(read_measurements(raw_lines), 9.0, 20.0), 2)

    pipeline = build_pipeline()
    print("первое:", next(pipeline))
    print("второе:", next(pipeline))
    print("остальные:", list(pipeline))
    print("повторный обход исчерпанного генератора:", list(pipeline))
    print("новый конвейер:", list(build_pipeline()))
    print("исходные строки не изменились:", raw_lines)

    print("--- Некорректное окно ---")
    try:
        list(moving_average([1, 2, 3], 0))
    except ValueError as error:
        print("Ошибка:", error)

    print("--- Включения ---")
    print([x * x for x in range(1, 21) if x % 2 == 0])
    print({len(s) for s in ["abc", "", "de", "fgh", "", "i"] if s})
    print({n: n * n for n in range(1, 11)})
    print(sum(x * x for x in range(1_000_000)))

    squares_list = [x * x for x in range(1_000_000)]
    squares_gen = (x * x for x in range(1_000_000))
    print("размер списка, байт:", sys.getsizeof(squares_list))
    print("размер генераторного выражения, байт:", sys.getsizeof(squares_gen))

    print("--- take, drop, batch ---")
    print(list(take(3, range(100))))
    print(list(drop(3, "abcdef")))
    print(list(batch(range(7), 3)))

    print("--- Конвейер + batch ---")
    more_lines = ["10.0", "", "12.5", "11.5", "13.0", "9.5", "14.0", "15.5", "100.0", "12.0", "11.0"]
    averages = moving_average(filter_range(read_measurements(more_lines), 9.0, 20.0), 2)
    for number, package in enumerate(batch(averages, 3), start=1):
        print("пакет", number, package)
    averages = moving_average(filter_range(read_measurements(more_lines), 9.0, 20.0), 2)
    print("пропустить 2, взять 3:", list(take(3, drop(2, averages))))

    print("--- tracemalloc (100 000 чисел) ---")
    lazy_total, lazy_peak = peak_memory_kb(lazy_run, 100_000)
    list_total, list_peak = peak_memory_kb(list_run, 100_000)
    print("ленивый конвейер: результат =", lazy_total, ", пик памяти, КБ =", round(lazy_peak, 1))
    print("конвейер из списков: результат =", list_total, ", пик памяти, КБ =", round(list_peak, 1))