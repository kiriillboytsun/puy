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
