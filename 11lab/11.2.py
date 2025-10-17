

import os
from PIL import Image

input_folder = "изо"
output_folder = "converted"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)

    with Image.open(input_path) as img:
        rgb_image = img.convert("RGB")
        rgb_image.save(output_path)

print("Обработка завершена.")