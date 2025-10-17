n = int(input("Введите количество слов: "))
result = ""
for i in range(n):
    word = input(f"Введите слово {i + 1}: ")
    if i == 0:
        result += word
    else:
        result += " " + word

print("Результат:", result)
