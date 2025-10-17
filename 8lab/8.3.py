students = {
    "Андрей": {"Английский", "Французский"},
    "Мария": {"Немецкий", "Китайский"},
    "Иван": {"Китайский", "Английский"},
    "Ольга": {"Испанский"},
    "Сергей": {"Французский", "Немецкий"}
}

all_languages = set()
chinese_speakers = []

for student, languages in students.items():
    all_languages.update(languages)
    if "Китайский" in languages:
        chinese_speakers.append(student)

print("Количество различных языков:", len(all_languages))
print("Список языков:", sorted(all_languages))
print("Студенты, знающие китайский язык:", chinese_speakers)
