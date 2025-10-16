color1 = input("Введите первый основной цвет (красный, синий, желтый): ").lower()
color2 = input("Введите второй основной цвет (красный, синий, желтый): ").lower()

primary_colors = {"красный", "синий", "желтый"}

if color1 not in primary_colors or color2 not in primary_colors:
    print("Ошибка: нужно ввести только основные цвета — красный, синий или желтый.")
elif color1 == color2:
    print(f"Вы ввели одинаковые цвета: {color1}. Результат — тот же цвет.")
else:
    if ("красный" in [color1, color2]) and ("синий" in [color1, color2]):
        print("Фиолетовый")
    elif ("красный" in [color1, color2]) and ("желтый" in [color1, color2]):
        print("Оранжевый")
    elif ("синий" in [color1, color2]) and ("желтый" in [color1, color2]):
        print("Зеленый")
