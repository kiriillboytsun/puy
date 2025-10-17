words = []

print("Вводите слова по одному. Чтобы остановиться, введите 'stop'.")

while True:
    word = input("Введите слово: ")
    if word.lower() == "stop":
        break
    words.append(word)

result = " ".join(words)
print("Результат:", result)
