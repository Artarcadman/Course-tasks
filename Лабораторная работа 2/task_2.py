salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0 # Подушка безопасности
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(months):
    actual_money = salary-spend
    spend *= (1+increase)
    if actual_money<0:
        money_capital += -(actual_money)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital,2))
