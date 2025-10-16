seat_number = int(input("Введите номер места (1-54): "))

if seat_number < 1 or seat_number > 54:
    print("Номер места должен быть от 1 до 54")
else:

    if seat_number >= 1 and seat_number <= 36:
        place_type = "купе"
    else:
        place_type = "боковое"

    if (seat_number % 2) == 0:
        level = "верхнее"
    else:
        level = "нижнее"

    print(f"{level} {place_type} место")
