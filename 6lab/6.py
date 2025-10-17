def lab1():
    def delna3(number):
        return number % 3 == 0

    num = int(input("Введите число: "))

    if delna3(num):
        print("Число делится на 3")
    else:
        print("Число не делится на 3")

def lab2():
    def divide_by_user_input():
        try:
            user_input = input("Введите число, на которое нужно разделить 100: ")
            number = float(user_input)
            result = 100 / number
            print("Результат деления:", result)
        except ValueError:
            print("Ошибка: нужно ввести число.")
        except ZeroDivisionError:
            print("Ошибка: деление на ноль.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

    divide_by_user_input()

def lab3():
    def is_magic_date(date_str):
        try:
            day, month, year = map(int, date_str.split('.'))
            return day * month == year % 100
        except ValueError:
            print("Ошибка: введите дату в формате ДД.ММ.ГГГГ")
            return False

    date_input = input("Введите дату в формате ДД.ММ.ГГГГ: ")

    if is_magic_date(date_input):
        print("Это магическая дата!")
    else:
        print("Это не магическая дата.")

def lab4():
    def is_lucky_ticket(ticket_number):
        if len(ticket_number) % 2 != 0 or not ticket_number.isdigit():
            print("Ошибка: номер должен быть строкой с чётным количеством цифр.")
            return False
        half = len(ticket_number) // 2
        first_half_sum = sum(int(d) for d in ticket_number[:half])
        second_half_sum = sum(int(d) for d in ticket_number[half:])
        return first_half_sum == second_half_sum

    number = input("Введите номер билета: ")

    if is_lucky_ticket(number):
        print("Это счастливый билет!")
    else:
        print("Увы, билет не счастливый.")

def main():
    while True:
        print("\nВыберите лабораторную работу:")
        print("1 — Проверка делимости на 3")
        print("2 — Деление 100 на введённое число")
        print("3 — Проверка магической даты")
        print("4 — Проверка счастливого билета")
        print("0 — Выход")

        choice = input("Введите номер: ")

        if choice == "1":
            lab1()
        elif choice == "2":
            lab2()
        elif choice == "3":
            lab3()
        elif choice == "4":
            lab4()
        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()