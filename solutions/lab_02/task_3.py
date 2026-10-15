import sys
import weakref
data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))


class Record:
    pass


record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())



registry = weakref.WeakValueDictionary()

r1 = Record()
r2 = Record()
r3 = Record()

registry["one"] = r1
registry["two"] = r2
registry["three"] = r3

del r3

print(list(registry.keys()))

del r2

print(list(registry.keys()))

del r1

print(list(registry.keys()))
