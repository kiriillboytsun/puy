import tkinter as tk
from tkinter import simpledialog, messagebox

class IceCreamStand:
    def __init__(self, name, location, hours, flavors):
        self.name = name
        self.location = location
        self.hours = hours
        self.flavors = flavors

    def get_info(self):
        return f"{self.name}\n{self.location}\nЧасы работы: {self.hours}"

    def get_flavors_text(self):
        return "\n".join(f"- {flavor}" for flavor in self.flavors)

    def add_flavor(self, flavor):
        if flavor and flavor not in self.flavors:
            self.flavors.append(flavor)
            return True
        return False

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            return True
        return False

def update_flavor_list():
    flavor_list.config(text=stand.get_flavors_text())

def add_flavor():
    new_flavor = simpledialog.askstring("Добавить вкус", "Введите название нового вкуса:")
    if new_flavor:
        if stand.add_flavor(new_flavor.strip()):
            update_flavor_list()
        else:
            messagebox.showinfo("Информация", "Такой вкус уже есть или введено пустое значение.")

def remove_flavor():
    flavor_to_remove = simpledialog.askstring("Удалить вкус", "Введите название вкуса для удаления:")
    if flavor_to_remove:
        if stand.remove_flavor(flavor_to_remove.strip()):
            update_flavor_list()
        else:
            messagebox.showinfo("Информация", "Такого вкуса нет в списке.")

stand = IceCreamStand(
    "BrandIce",
    "просп. Просвещения, 32, корп. 1",
    "10:00–22:00",
    ["Ванильное", "Шоколадное", "Клубничное", "Фисташковое"]
)

root = tk.Tk()
root.title("Кафе мороженое")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

info_label = tk.Label(frame, text=stand.get_info(), font=("Arial", 14), justify="left")
info_label.pack(anchor="w")

flavor_title = tk.Label(frame, text="\nДоступные вкусы:", font=("Arial", 12, "bold"))
flavor_title.pack(anchor="w")

flavor_list = tk.Label(frame, text=stand.get_flavors_text(), font=("Arial", 12), justify="left")
flavor_list.pack(anchor="w")

button_frame = tk.Frame(frame, pady=10)
button_frame.pack(anchor="w")

add_button = tk.Button(button_frame, text="Добавить вкус", command=add_flavor)
add_button.pack(side="left", padx=(0, 10))

remove_button = tk.Button(button_frame, text="Удалить вкус", command=remove_flavor)
remove_button.pack(side="left")

root.mainloop()
