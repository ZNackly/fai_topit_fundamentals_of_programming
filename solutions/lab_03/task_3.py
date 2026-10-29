submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]

students = set()
labs = set()
student_attempts = dict()
best = {}
attempt_counts = {}
students_by_lab = {}

for student, lab, score in submissions:
    students.add(student)
    labs.add(lab)
    student_attempts.setdefault(student, []).append((lab, score))
    students_by_lab.setdefault(lab, set()).add(student)

    key = (student, lab)
    if key not in best or score > best[key]:
        best[key] = score
    attempt_counts[key] = attempt_counts.get(key, 0) + 1

print(students)
print(labs)
print(student_attempts)
print(best)
print(attempt_counts)

students_lab01 = {name for name, lab, score in submissions if lab == "lab_01"}
students_lab02 = {name for name, lab, score in submissions if lab == "lab_02"}
both_labs = students_lab01 & students_lab02


def add_submission(student, lab, score):
    students.add(student)
    labs.add(lab)
    student_attempts.setdefault(student, []).append((lab, score))
    students_by_lab.setdefault(lab, set()).add(student)

    key = (student, lab)
    if key not in best or score > best[key]:
        best[key] = score
    attempt_counts[key] = attempt_counts.get(key, 0) + 1


add_submission("daria", "lab_02", 5)
print("После добавления:")
print(best.get(("daria", "lab_02")))
print(attempt_counts.get(("daria", "lab_02")))


def run_query(query):
    parts = query.strip().split()
    if not parts:
        print("Пустой запрос")
        return

    cmd, args = parts[0].lower(), parts[1:]

    if cmd == "student":
        if len(args) != 1:
            print("Использование: student <имя>")
            return
        name = args[0]
        if name in students:
            print(f"Студент '{name}' найден")
        else:
            print(f"Студент '{name}' не найден")

    elif cmd == "best":
        if len(args) != 2:
            print("Использование: best <имя> <lab>")
            return
        key = (args[0], args[1])
        if key in best:
            print(f"Лучший результат {key[0]} по {key[1]}: {best[key]}")
        else:
            print(f"Нет данных для {key[0]} / {key[1]}")

    elif cmd == "attempts":
        if len(args) != 2:
            print("Использование: attempts <имя> <lab>")
            return
        key = (args[0], args[1])
        if key in attempt_counts:
            print(f"Попыток {key[0]} по {key[1]}: {attempt_counts[key]}")
        else:
            print(f"Нет попыток для {key[0]} / {key[1]}")

    elif cmd == "completed":
        if len(args) != 1:
            print("Использование: completed <lab>")
            return
        lab = args[0]
        if lab in students_by_lab:
            print(f"Работу {lab} сдавали: {sorted(students_by_lab[lab])}")
        else:
            print(f"Работа '{lab}' не найдена")

    else:
        print(f"Неизвестная команда: '{cmd}'")


for q in [
    "student anna",
    "best anna lab_01",
    "attempts boris lab_02",
    "completed lab_01",
    "best kolya lab_09",
    "unknown x",
]:
    print(">", q)
    run_query(q)