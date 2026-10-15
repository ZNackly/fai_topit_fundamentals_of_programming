from sys import getsizeof
import tracemalloc
print("Часть 1")
empty = list()
list10 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tuple10 = tuple([1, 2, 4, 5, 6, 7, 8, 9])
string10 = "0123456789"
integer = 1234567890
none = None
print(getsizeof(empty))
print(getsizeof(list10))
print(getsizeof(tuple10))
print(getsizeof(string10))
print(getsizeof(integer))
print(getsizeof(none))
print("\nЧасть2")
list100 = []
sizeof100 = getsizeof(list100)
for i in range(100):
    list100.append(i)
    if getsizeof(list100) != sizeof100:
        sizeof100 = getsizeof(list100)
        print(len(list100), sizeof100)
print("\nЧасть 3")
tracemalloc.start()
list_range_100k = list(range(100_000))
print(f"Текущая память: {tracemalloc.get_traced_memory()[0]/1024} КБ Пиковая память: {tracemalloc.get_traced_memory()[0]/1024} КБ")
tracemalloc.stop()
tracemalloc.start()
range_100k = range(100_000)
print(f"Текущая память: {tracemalloc.get_traced_memory()[0]/1024} КБ Пиковая память: {tracemalloc.get_traced_memory()[0]/1024} КБ")
tracemalloc.stop()

