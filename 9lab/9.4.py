import os
from PIL import Image, ImageDraw, ImageFont

p = "с_водяным_знаком"
os.makedirs(p, exist_ok=True)

w = "©kiri"

f = ImageFont.truetype("/Windows/Fonts/arial.ttf", 70)

for n in range(1, 6):
    file_path = f"/Users/xnx/Desktop/лабы/изо/{n}.jpg"
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        continue
    i = Image.open(file_path).convert("RGBA")
    l = Image.new("RGBA", i.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(l)

    x, y = i.size

    bbox = d.textbbox((0, 0), w, font=f)
    tx = bbox[2] - bbox[0]
    ty = bbox[3] - bbox[1]

    step_x = tx + 100
    step_y = ty + 50

    for px in range(0, x, step_x):
        for py in range(0, y, step_y):
            d.text((px, py), w, font=f, fill=(255, 255, 255, 60))

    r = Image.alpha_composite(i, l).convert("RGB")
    r.save(f"{p}/водяной_{n}.jpg")

print("Готово! Водяной знак размещён по всей поверхности.")