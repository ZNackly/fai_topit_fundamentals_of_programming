from task_2 import StepRange


def consume(iterable) -> list:
    result = []
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        result.append(item)
    return result


def my_enumerate(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1


def my_zip(first, second):
    first_iterator = iter(first)
    second_iterator = iter(second)
    while True:
        try:
            a = next(first_iterator)
            b = next(second_iterator)
        except StopIteration:
            return
        yield a, b


def numbers_generator():
    yield 1
    yield 2
    yield 3


if __name__ == "__main__":
    values = [10, 20, 30]
    iterator = iter(values)

    print(iterator is values)
    print(iter(iterator) is iterator)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    # print(next(iterator))

    print("--- consume ---")
    print(consume([1, 2, 3]))
    print(consume((4, 5, 6)))
    print(consume("abc"))
    print(consume(range(3)))
    partly_used = iter([1, 2, 3, 4, 5])
    next(partly_used)
    next(partly_used)
    print(consume(partly_used))

    print("--- Повторный обход списка и его итератора ---")
    data = [1, 2, 3]
    print("список, 1-й раз:", consume(data))
    print("список, 2-й раз:", consume(data))
    data_iterator = iter(data)
    print("итератор, 1-й раз:", consume(data_iterator))
    print("итератор, 2-й раз:", consume(data_iterator))

    print("--- my_enumerate ---")
    print(list(my_enumerate(["a", "b", "c"])))
    print(list(my_enumerate("xy", start=1)))
    print(list(my_enumerate(numbers_generator(), start=10)))
    print(list(my_enumerate(StepRange(0, 10, 5))))

    print("--- my_zip ---")
    print(list(my_zip([1, 2, 3], "ab")))
    print(list(my_zip("abc", numbers_generator())))
    print(list(my_zip(StepRange(0, 10, 3), [10, 20, 30, 40, 50])))
    print(list(my_zip([], [1, 2])))