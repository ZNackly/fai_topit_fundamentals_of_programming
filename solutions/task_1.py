print("=== Обработка одной записи ===")

score = int(input("Результат (0–100): "))
if not (0 <= score <= 100):
    print(f"Ошибка: результат {score} вне диапазона 0–100.")
else:
    work_type = input("Тип работы (exam/project/practice): ").strip()
    if work_type not in ("exam", "project", "practice"):
        print(f"Ошибка: неизвестный тип работы '{work_type}'.")
    else:
        absences = int(input("Пропущено занятий (0–5): "))
        if not (0 <= absences <= 5):
            print(f"Ошибка: количество пропусков {absences} вне диапазона 0–5.")
        else:
            if 90 <= score <= 100:
                level = "отличный"
            elif 75 <= score <= 89:
                level = "хороший"
            elif 60 <= score <= 74:
                level = "удовлетворительный"
            else:
                level = "недостаточный"

            levels = ["недостаточный", "удовлетворительный", "хороший", "отличный"]
            if absences > 3:
                idx = levels.index(level)
                if idx > 0:
                    level = levels[idx - 1]

            match work_type:
                case "exam":
                    explanation = "экзаменационная работа"
                case "project":
                    explanation = "проектная работа"
                case "practice":
                    explanation = "практическая работа"

            print(f"score={score}, тип={work_type} ({explanation}), "
                  f"пропуски={absences} -> уровень: {level}")


print("\n=== Обработка списка записей ===")
records = [
    (100, "exam", 0),
    (90, "project", 4),
    (89, "practice", 1),
    (75, "exam", 5),
    (74, "project", 0),
    (60, "practice", 4),
    (59, "exam", 1),
    (0,  "project", 0),
    (85, "lecture", 2),
    (95, "exam", 7),
    (101, "exam", 0),
]

source = list(records)

summary = {"отличный": 0, "хороший": 0,
           "удовлетворительный": 0, "недостаточный": 0}

print("\nИндивидуальные результаты:")
i = 1
for record in source:
    score, type, absences = record

    if not (0 <= score <= 100):
        line = f"Ошибка: результат {score} вне диапазона 0–100."
    elif type not in ("exam", "project", "practice"):
        line = f"Ошибка: неизвестный тип работы '{type}'."
    elif not (0 <= absences <= 5):
        line = f"Ошибка: количество пропусков {absences} вне диапазона 0–5."
    else:
        if 90 <= score <= 100:
            level = "отличный"
        elif 75 <= score <= 89:
            level = "хороший"
        elif 60 <= score <= 74:
            level = "удовлетворительный"
        else:
            level = "недостаточный"

        levels = ["недостаточный", "удовлетворительный", "хороший", "отличный"]
        if absences > 3:
            idx = levels.index(level)
            if idx > 0:
                level = levels[idx - 1]

        match type:
            case "exam":
                explanation = "экзаменационная работа"
            case "project":
                explanation = "проектная работа"
            case "practice":
                explanation = "практическая работа"

        line = (f"score={score}, тип={type} ({explanation}), "
                f"пропуски={absences} -> уровень: {level}")
        summary[level] += 1

    print(f"{i:>2}. {line}")
    i += 1

print("\nИтоговая сводка по уровням:")
for lvl, cnt in summary.items():
    print(f"  {lvl:<20} : {cnt}")