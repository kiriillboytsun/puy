class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0

    def describe_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' предлагает {self.cuisine_type}.")

    def update_rating(self, new_rating):
        self.rating = new_rating


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print("Доступные вкусы мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream_stand = IceCreamStand("brb", "Десерты", ["ванильное", "шоколадное", "клубничное"])
ice_cream_stand.describe_restaurant()
ice_cream_stand.show_flavors()
