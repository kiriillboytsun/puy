countries = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Германия": "Берлин",
    "Италия": "Рим",
    "Япония": "Токио"
}

print("Список стран и столиц:")
for country, capital in countries.items():
    print(f"{country} — {capital}")

search_country = input("Введите название страны, чтобы узнать её столицу: ")
capital = countries.get(search_country)
if capital:
    print(f"Столица страны {search_country} — {capital}")
else:
    print("Такой страны нет в словаре.")

print("\nСтраны и столицы в алфавитном порядке:")
for country in sorted(countries):
    print(f"{country} — {countries[country]}")
