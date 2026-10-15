import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)
original.append(["Databases", 5])
print("original:")
print(original)
print("alias:")
print(alias)
print("shallow:")
print(shallow)
print("deep:")
print(deep)
print()
original[0][1] = 3
print("original:")
print(original)
print("alias:")
print(alias)
print("shallow:")
print(shallow)
print("deep:")
print(deep)
print()
print("id внешних списков:")
print("original:", id(original))
print("alias:   ", id(alias))
print("shallow: ", id(shallow))
print("deep:    ", id(deep))
print()
print("id первого вложенного списка:")
print("original:", id(original[0]))
print("alias:   ", id(alias[0]))
print("shallow: ", id(shallow[0]))
print("deep:    ", id(deep[0]))
print()
print("id объекта, содержащего первую оценку:")
print("original:", id(original[0][1]))
print("alias:   ", id(alias[0][1]))
print("shallow: ", id(shallow[0][1]))
print("deep:    ", id(deep[0][1]))
print()
wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1
print("wrong_matrix:")
print(wrong_matrix)
print()
correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1
print("correct_matrix:")
print(correct_matrix)