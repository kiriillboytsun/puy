from PIL import Image, ImageOps

image_path = "/Users/xnx/Desktop/лабы/изо/11.jpeg"
try:
    image = Image.open(image_path)

    resized = image.resize((image.width // 3, image.height // 3))
    resized.save("example_resized.jpg")

    flipped_horizontal = ImageOps.mirror(image)
    flipped_horizontal.save("example_flipped_horizontal.jpg")

    flipped_vertical = ImageOps.flip(image)
    flipped_vertical.save("example_flipped_vertical.jpg")

    print("Изображения успешно сохранены.")
except FileNotFoundError:
    print(f"Файл {image_path} не найден.")
