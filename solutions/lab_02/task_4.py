import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print(gc.isenabled())
print(gc.get_threshold())
stats = gc.get_stats()

for stat in stats:
    print(stat)
print(id(first))
print(id(second))
del first
del second

print(gc.collect())

gc.disable()

a = []
b = []
c = []

a.append(b)
b.append(c)
c.append(a)

del a
del b
del c
print(gc.collect())
gc.enable()

A = {"name" : "A", "spisok" : []}
B = {"name" : "B", "spisok" : []}
C = {"name" : "C", "spisok" : []}
D = {"name" : "D", "spisok" : []}

A["spisok"].append(B)
B["spisok"].append(C)
C["spisok"].append(A)

print(f"{A['name']} связан с {A['spisok'][0]['name']}")
print(f"{B['name']} связан с {B['spisok'][0]['name']}")
print(f"{C['name']} связан с {C['spisok'][0]['name']}")


del A
del B
del C

print(f"D = {D}")







