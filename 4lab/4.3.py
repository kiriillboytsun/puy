def visokosniy(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Введите год: "))

if visokosniy(year):
    print(f"Год {year} - високосный")
else:
    print("Это год не високосный")
