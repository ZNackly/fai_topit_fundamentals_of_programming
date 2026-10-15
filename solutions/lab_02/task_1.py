print("ЭКСПЕРИМЕНТ A")
print()

a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))

print()
print("ЭКСПЕРИМЕНТ B")
print()
first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))
print()
second.append(30)

print(first, second)
print(id(first), id(second))
print()

second = [10, 20, 30]

print("first= ", first)
print("second= ", second)
print("id(first)= ", id(first))
print("id(second)= ", id(second))
print("first is second: ", first is second)
print()

print("first == second: ", first == second)
print("first is second: ", first is second)


second.append(40)

print("first= ", first)
print("second= ", second)
print("first is second: ", first is second)
print()
config_1 = {
    "name": "Учебный проект",
    "participants": ["Анна", "Борис", "Виктор"],
    "run_params": ["timeout=30"],
}

config_2 = config_1
print("До изменений:")
print("config_1 =", config_1)
print("config_2 =", config_2)
print()
config_2["participants"].append("Галина")
print("Зависимая копия:")
print("config_1 =", config_1)
print("config_2 =", config_2)

config_1 = {
    "name": "Учебный проект",
    "participants": ["Анна", "Борис", "Виктор", "Галина"],
    "run_params": ["timeout=30"],
}


config_2["name"] = "Учебный проект 2"
print()
print("Независимая копия:")
print("config_1 =", config_1)
print("config_2 =", config_2)
assert config_1 is not config_2, "config_1 и config_2 ссылаются на одинаковые объекты"


