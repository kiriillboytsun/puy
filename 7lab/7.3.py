week_days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

count = int(input("Сколько выходных на неделе вы хотите? "))

if 0 <= count <= 7:
    weekends = list(week_days[-count:]) if count > 0 else []
    weekdays = list(week_days[:-count]) if count > 0 else list(week_days)

    print("Ваши выходные дни:", weekends)
    print("Ваши рабочие дни:", weekdays)
else:
    print("Ошибка: в неделе 7 дней.")
