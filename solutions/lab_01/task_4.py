student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10
percent= 100 * (completed/total)
symbol = "Я"
print(student[0])
print(student[-1])
print(student[0:4])
print(student[5:-1])
print(student.lower())
print(student.upper())
print(student[0]+ "." + student[5]+".")
print(course[::-1])
print("%s — %s: %d/%d (%.1f%%)" % (student, course, completed, total, percent))
print("{} — {}: {}/{} ({:.1f}%)".format(student, course, completed, total, percent))
print(f"{student} — {course}: {completed}/{total} ({percent:.1f}%)")
print(symbol)
print(ord(symbol))
print(chr(ord(symbol)))
print(symbol.encode("utf-8"))
print(len(symbol.encode("utf-8")))
# course[0] = symbol