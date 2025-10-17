import json

file = open('products.json', encoding='utf-8')
data = json.load(file)
file.close()

name = input("Название: ")
price = float(input("Цена: "))
weight = float(input("Вес: "))
available_input = input("В наличии?: ").strip().lower()
available = available_input == "да"

new_product = {
    "name": name,
    "price": price,
    "weight": weight,
    "available": available
}

data["products"].append(new_product)

file = open('products.json', 'w', encoding='utf-8')
json.dump(data, file, ensure_ascii=False, indent=4)
file.close()

print("\nСписок продуктов:")
for p in data["products"]:
    print(f"Название: {p['name']}")
    print(f"Цена: {p['price']}")
    print(f"Вес: {p['weight']}")
    if p["available"]:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()