import os
from PIL import Image, ImageEnhance

input_folder = "изо"
output_folder = "processed_images"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with Image.open(input_path) as img:
            enhancer = ImageEnhance.Brightness(img)
            enhanced_img = enhancer.enhance(1.5)

            enhanced_img.save(output_path)

print(f"Обработка завершена. Файлы сохранены в папке: {output_folder}")