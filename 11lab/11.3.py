import csv

filename = "lab.csv"
total = 0

print("Нужно купить:")

with open(filename, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        row = {key.strip(): value.strip() for key, value in row.items()}
        product = row["Продукт"]
        quantity = int(row["Количество"])
        price = int(row["Цена"])
        total += quantity * price
        print(f"{product.capitalize()} - {quantity} шт. за {price} руб.")

print(f"Итоговая сумма: {total} руб")
