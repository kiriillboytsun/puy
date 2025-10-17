class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0

    def describe_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' предлагает блюда {self.cuisine_type} кухни.")

    def update_rating(self, new_rating):
        self.rating = new_rating


r = Restaurant("Гурман", "Французская")
r.describe_restaurant()
print(f"Начальный рейтинг: {r.rating}")
r.update_rating(4.8)
print(f"Обновлённый рейтинг: {r.rating}")
