import random

numbers = random.sample(range(1, 51), 5)
user_input = int(input("Введите число: "))

print("Исходный список:", numbers)
print("Ваше число:", user_input)

if user_input in numbers:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")