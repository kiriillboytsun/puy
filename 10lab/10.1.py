from PIL import Image

image = Image.open("/Users/xnx/Desktop/лабы/открытка/mm.jpg")

width, height = image.size
print("Размер изображения:", width, "x", height)

left = int(width * 0.78)
upper = int(height * 0.33)
right = width
lower = int(height * 0.67)
crop_area = (left, upper, right, lower)
cropped_image = image.crop(crop_area)

cropped_image.save("/Users/xnx/Desktop/лабы/открытка/mm_обрезан.jpg")
print("Готово! Сохранено как '/Users/xnx/Desktop/лабы/открытка/mm_обрезан.jpg'")
