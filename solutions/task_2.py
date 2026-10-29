import random

measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

total = 0
minimum = measurements[0]
maximum = measurements[0]
even_count = 0

for x in measurements:
    total += x
    if x < minimum:
        minimum = x
    if x > maximum:
        maximum = x
    if x % 2 == 0:
        even_count += 1

average = total / len(measurements)

above_average = 0
for x in measurements:
    if x > average:
        above_average += 1

print("=== Статистика измерений ===")
print(f"Сумма: {total}")
print(f"Минимум: {minimum}")
print(f"Максимум: {maximum}")
print(f"Чётных значений: {even_count}")
print(f"Среднее арифметическое: {average:.2f}")
print(f"Значений выше среднего: {above_average}")

target = int(input("\nВведите число для поиска: "))

position = -1
for i in range(len(measurements)):
    if measurements[i] == target:
        position = i
        break

if position == -1:
    print(-1)
else:
    print(f"Первое вхождение числа {target}: индекс {position}")


def is_prime(n):
    if n == 1 or n < 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

number = int(input("\nВведите положительное целое число для проверки простоты: "))
if is_prime(number):
    print(f"{number} — простое число")
else:
    print(f"{number} — не является простым числом")


def selection_sort(arr):
    a = list(arr)
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a


def linear_search_count(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons


def binary_search_count(arr, target):
    comparisons = 0
    left = 0
    right = len(arr) - 1
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons


print("\n=== Сравнение линейного и бинарного поиска ===")
print(f"{'Размер':>8} | {'Цель':>6} | {'Лин. сравн.':>12} | {'Бин. сравн.':>12}")
print("-" * 50)

sizes = [10, 100, 1000]
random.seed(42)

for size in sizes:
    data = [random.randint(1, size * 10) for _ in range(size)]
    sorted_data = selection_sort(data)
    target = sorted_data[-1]

    _, lin_cmp = linear_search_count(data, target)
    _, bin_cmp = binary_search_count(sorted_data, target)

    print(f"{size:>8} | {target:>6} | {lin_cmp:>12} | {bin_cmp:>12}")

print("\nПоиск отсутствующего элемента:")
print(f"{'Размер':>8} | {'Лин. сравн.':>12} | {'Бин. сравн.':>12}")
print("-" * 40)
for size in sizes:
    data = [random.randint(1, size * 10) for _ in range(size)]
    sorted_data = selection_sort(data)
    _, lin_cmp = linear_search_count(data, -1)
    _, bin_cmp = binary_search_count(sorted_data, -1)
    print(f"{size:>8} | {lin_cmp:>12} | {bin_cmp:>12}")