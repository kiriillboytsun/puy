import random
from PIL import Image, ImageDraw, ImageFont

image_path = "cat.jpg"
image = Image.open(image_path).convert("RGBA")

draw = ImageDraw.Draw(image)

name = input("Введите имя того, кого вы хотите поздравить: ")

text = f"{name}, поздравляю!"

font_paths = [
    "/Windows/Fonts/arial.ttf",
    "/Windows/Fonts/times.ttf",
    "/Windows/Fonts/verdana.ttf"
]
fonts = [ImageFont.truetype(path, 60) for path in font_paths]

image_width, image_height = image.size
x = image_width / 2
y = image_height - 100

chars = list(text)

total_width = 0
char_sizes = []
for char in chars:
    font = random.choice(fonts)
    bbox = draw.textbbox((0, 0), char, font=font)
    width = bbox[2] - bbox[0]
    char_sizes.append((char, font, width))
    total_width += width

x_start = (image_width - total_width) / 2

colors = [
    (255, 0, 0),
    (0, 128, 255),
    (0, 200, 0),
    (255, 165, 0),
    (128, 0, 128)
]

x_pos = x_start
for i, (char, font, width) in enumerate(char_sizes):
    color = colors[i % len(colors)]
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]
    for dx, dy in offsets:
        draw.text((x_pos + dx, y + dy), char, font=font, fill=color)
    x_pos += width

output_path = "greeting_card.png"
image.save(output_path)

print(f"Открытка успешно сохранена в файл '{output_path}'")
