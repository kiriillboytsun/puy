def delna3(number):
    return number % 3 == 0

num = int(input("Введите число: "))

if delna3(num):
    print("Число делится на 3")
else:
    print("Число не делится на 3")
