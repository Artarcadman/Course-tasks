users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

total_amount = {"Общее количество": 0, "Уникальные посещения": 0}
total_amount["Общее количество"] = len(users)
total_amount["Уникальные посещения"] = len(set(users))
print(total_amount)
