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
