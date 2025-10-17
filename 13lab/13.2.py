

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print()

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")


r1 = Restaurant("Sushi wont", "Японская")
r2 = Restaurant("Русские сказки", "Русская домашняя")
r3 = Restaurant("Taco Fiesta", "Мексиканская")

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()