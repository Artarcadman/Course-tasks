money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0 # Количество месяцев
actual_money = money_capital + salary - spend # Деньги, которые остаются в конце месяца
while actual_money >=0:
    spend *= 1+increase
    actual_money = actual_money + salary - spend
    months+=1

print("Количество месяцев, которое можно протянуть без долгов:", months)
