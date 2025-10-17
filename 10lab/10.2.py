from PIL import Image

postcards = {
    "Новый год": "нг.webp",
    "День рождения": "др.jpg",
    "9 мая": "9май.jpg",
    "1 сентября": "дз.jpg",
}

holiday_list = ", ".join(postcards.keys())
holiday = input(f"К какому празднику вам нужна открытка? ({holiday_list})\n")

normalized_holiday = holiday.lower()
match = None
for key in postcards:
    if key.lower() == normalized_holiday:
        match = key
        break

if match:
    image_path = f"/Users/xnx/Desktop/лабы/праздники/{postcards[match]}"
    try:
        image = Image.open(image_path)
        image.show()
    except FileNotFoundError:
        print(f"Файл {image_path} не найден.")
else:
    print("К сожалению, открытка к такому празднику отсутствует.")
