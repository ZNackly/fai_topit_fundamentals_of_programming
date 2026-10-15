import sys
import tracemalloc

empty = list()
list10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple10 = tuple([1, 2, 4, 5, 6, 7, 8, 9, 10])
string10 = "0123456789"
integer = 1234567890
none = None

results = []

tracemalloc.start()
obj = list()
current_e, peak_e = tracemalloc.get_traced_memory()
tracemalloc.stop()
results.append({
    "name": "empty",
    "n_elements": len(obj),
    "size_bytes": sys.getsizeof(obj),
    "current_bytes": current_e,
    "peak_bytes": peak_e,
})

tracemalloc.start()
obj = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
current_l, peak_l = tracemalloc.get_traced_memory()
tracemalloc.stop()
results.append({
    "name": "list10",
    "n_elements": len(obj),
    "size_bytes": sys.getsizeof(obj),
    "current_bytes": current_l,
    "peak_bytes": peak_l,
})

tracemalloc.start()
obj = tuple([1, 2, 4, 5, 6, 7, 8, 9, 10])
current_t, peak_t = tracemalloc.get_traced_memory()
tracemalloc.stop()
results.append({
    "name": "tuple10",
    "n_elements": len(obj),
    "size_bytes": sys.getsizeof(obj),
    "current_bytes": current_t,
    "peak_bytes": peak_t,
})

tracemalloc.start()
obj = "0123456789"
current_s, peak_s = tracemalloc.get_traced_memory()
tracemalloc.stop()
results.append({
    "name": "string10",
    "n_elements": len(obj),
    "size_bytes": sys.getsizeof(obj),
    "current_bytes": current_s,
    "peak_bytes": peak_s,
})

tracemalloc.start()
obj = 1234567890
current_i, peak_i = tracemalloc.get_traced_memory()
tracemalloc.stop()
results.append({
    "name": "integer",
    "n_elements": 1,
    "size_bytes": sys.getsizeof(obj),
    "current_bytes": current_i,
    "peak_bytes": peak_i,
})

tracemalloc.start()
obj = None
current_n, peak_n = tracemalloc.get_traced_memory()
tracemalloc.stop()
results.append({
    "name": "none",
    "n_elements": 1,
    "size_bytes": sys.getsizeof(obj),
    "current_bytes": current_n,
    "peak_bytes": peak_n,
})

tracemalloc.start()
list_range_100k = list(range(100_000))
current_lr, peak_lr = tracemalloc.get_traced_memory()
tracemalloc.stop()
results.append({
    "name": "list_range_100k",
    "n_elements": 100_000,
    "size_bytes": sys.getsizeof(list_range_100k),
    "current_bytes": current_lr,
    "peak_bytes": peak_lr,
})

tracemalloc.start()
range_100k = range(100_000)
current_r, peak_r = tracemalloc.get_traced_memory()
tracemalloc.stop()
results.append({
    "name": "range_100k",
    "n_elements": 100_000,
    "size_bytes": sys.getsizeof(range_100k),
    "current_bytes": current_r,
    "peak_bytes": peak_r,
})

print("=" * 78)
print("ИТОГОВЫЙ ОТЧЁТ")
print("=" * 78)
print(
    f"{'сценарий':<22}"
    f"{'элементов':>10}"
    f"{'размер, КиБ':>14}"
    f"{'текущая, КиБ':>16}"
    f"{'пик, КиБ':>12}"
)
print("-" * 78)
for r in results:
    print(
        f"{r['name']:<22}"
        f"{r['n_elements']:>10}"
        f"{r['size_bytes'] / 1024:>14.4f}"
        f"{r['current_bytes'] / 1024:>16.4f}"
        f"{r['peak_bytes'] / 1024:>12.4f}"
    )
print()

print("=" * 78)
print("ОТНОШЕНИЕ ПИКОВ")
print("=" * 78)
print(f"  пик 'list_range_100k': {peak_lr / 1024:.4f} КиБ")
print(f"  пик 'range_100k': {peak_r / 1024:.4f} КиБ")
print(f"  отношение: {peak_lr / peak_r:.1f}×")