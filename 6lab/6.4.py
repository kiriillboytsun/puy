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
