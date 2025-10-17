numbers = [5, 8, 3, 5, 2, 8, 10]
seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

if duplicates:
    print("Найдены повторяющиеся элементы:", duplicates)
else:
    print("Повторяющихся элементов нет.")
