a = 1000
b = a
c = int("1000")

print("Типы:", type(a).__name__, type(b).__name__, type(c).__name__)
print("Идентификаторы:", id(a), id(b), id(c))
print("a == b:", a == b)
print("a is b:", a is b)
print("a == c:", a == c)
print("a is c:", a is c)

c = None

print(c is None)
print()
first = "python"
second = "py" + "thon"

print(first == second)
print(first is second)