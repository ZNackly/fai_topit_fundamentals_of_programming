"""
Программа запрашивает у пользователя имя исследователя, название эксперимента,
количество запусков, длительность одного запуска и комплексный коэффициент,
после чего вычисляет общую длительность, квадрат модуля коэффициента
и проверяет, выполнялись ли запуски.
"""
username = input()
experiment = input()
launches = int(input())
time = float(input())
real = float(input())
imag = float(input())

final_time = launches * time
final_time_minutes = final_time // 60
complex = complex(real=real, imag=imag)
sqr = real ** 2 + imag ** 2
has_runs = bool(launches)

print("========================================")
print(f'ЭКСПЕРИМЕНТ: {experiment}')
print(f'Исследователь: {username}')
print(f'Запуски: {launches}')
print(f"Общее время: {final_time:.2f} с ({final_time_minutes:.2f} мин)")
print(f"Коэффициент: ({complex})")
print(f"Квадрат модуля: {sqr:.2f}")
print(f"Есть выполненные запуски: {has_runs}")
print("========================================")

print("++++++++++++++++++++++++++++++++++++++++")
print("Типы введённых значений:")
print(f"username: {type(username).__name__}")
print(f"experiment: {type(experiment).__name__}")
print(f"launches: {type(launches).__name__}")
print(f"time: {type(time).__name__}")
print(f"real: {type(real).__name__}")
print(f"imag: {type(imag).__name__}")
print("++++++++++++++++++++++++++++++++++++++++")