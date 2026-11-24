class StepRangeIterator:
    def __init__(self, start: int, stop: int, step: int) -> None:
        self._current = start
        self._stop = stop
        self._step = step

    def __iter__(self) -> "StepRangeIterator":
        return self

    def __next__(self) -> int:
        if self._step > 0 and self._current >= self._stop:
            raise StopIteration
        if self._step < 0 and self._current <= self._stop:
            raise StopIteration

        value = self._current
        self._current += self._step
        return value


class StepRange:
    def __init__(self, start: int, stop: int, step: int = 1) -> None:
        if step == 0:
            raise ValueError("Шаг не может быть нулевым.")
        self._start = start
        self._stop = stop
        self._step = step

    def __iter__(self) -> StepRangeIterator:
        return StepRangeIterator(self._start, self._stop, self._step)

    def __len__(self) -> int:
        if self._step > 0:
            if self._start >= self._stop:
                return 0
            return (self._stop - self._start + self._step - 1) // self._step
        if self._start <= self._stop:
            return 0
        return (self._start - self._stop - self._step - 1) // (-self._step)

    def __contains__(self, value: object) -> bool:
        if not isinstance(value, int):
            return False
        if self._step > 0:
            if not self._start <= value < self._stop:
                return False
        else:
            if not self._stop < value <= self._start:
                return False
        return (value - self._start) % self._step == 0

    def __repr__(self) -> str:
        return f"StepRange({self._start}, {self._stop}, {self._step})"


if __name__ == "__main__":
    numbers = StepRange(2, 11, 3)
    iterator_a = iter(numbers)
    iterator_b = iter(numbers)

    print("StepRange:", numbers)
    print("list:", list(numbers))
    print("len:", len(numbers))
    print("8 in numbers:", 8 in numbers)
    print("7 in numbers:", 7 in numbers)

    print("--- Независимые итераторы ---")
    print("A:", next(iterator_a), "B:", next(iterator_b))
    print("A:", next(iterator_a), "B:", next(iterator_b))
    print("A:", next(iterator_a), "B:", next(iterator_b))

    print("--- Граничные случаи ---")
    print(list(StepRange(0, 5, 1)))
    print(list(StepRange(5, 0, -1)))
    print(list(StepRange(0, 0, 1)))
    print(list(StepRange(0, 5, -1)))

    print("--- Проверка нулевого шага ---")
    try:
        StepRange(0, 5, 0)
    except ValueError as error:
        print(error)
