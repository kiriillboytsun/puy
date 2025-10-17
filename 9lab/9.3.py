import os
from PIL import Image, ImageFilter

input_folder = "/Users/xnx/Desktop/лабы/изо"
output_folder = "filtered_images"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for i in range(1, 6):
    input_path = os.path.join(input_folder, f"{i}.jpg")
    output_path = os.path.join(output_folder, f"{i}_filtered.jpg")

    try:
        image = Image.open(input_path)
        filtered_image = image.filter(ImageFilter.CONTOUR)
        filtered_image.save(output_path)
        print(f"Файл {i}.jpg обработан и сохранён как {output_path}")
    except FileNotFoundError:
        print(f"Файл {i}.jpg не найден.")
