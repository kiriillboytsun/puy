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
    def __init__(self, restaurant_name, cuisine_type, flavors, location, hours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.hours = hours
        self.ice_cream_types = {}

    def show_flavors(self):
        print("Доступные вкусы мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)

    def has_flavor(self, flavor):
        return flavor in self.flavors

    def add_type(self, ice_type, flavors):
        self.ice_cream_types[ice_type] = flavors

    def show_types(self):
        print("Типы мороженого:")
        for ice_type, flavors in self.ice_cream_types.items():
            print(f"{ice_type}: {', '.join(flavors)}")

stand = IceCreamStand("BrandIce", "Десерты", ["ванильное", "шоколадное"], "просп. Просвещения, 32, корп. 1", "10:00–22:00")
stand.describe_restaurant()
print(f"Локация: {stand.location}")
print(f"Часы работы: {stand.hours}")
stand.show_flavors()
stand.add_flavor("фисташковое")
stand.remove_flavor("шоколадное")
print("Фисташковое есть?", "Да" if stand.has_flavor("фисташковое") else "Нет")
stand.show_flavors()
stand.add_type("мороженое на палочке", ["клубничное", "лимонное"])
stand.add_type("мягкое мороженое", ["ванильное", "шоколадное"])
stand.show_types()
