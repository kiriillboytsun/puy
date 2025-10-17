from PIL import Image

image_path = "/Users/xnx/Desktop/лабы/изо/11.jpeg"
try:
    image = Image.open(image_path)
    image.show()

    print("Размер изображения:", image.size)
    print("Формат изображения:", image.format)
    print("Цветовая модель:", image.mode)
except FileNotFoundError:
    print(f"Файл {image_path} не найден. Убедитесь, что он находится в нужной папке.")