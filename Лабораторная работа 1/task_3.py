list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

len_players = len(list_players)
team_len = len_players//2
first_team = list_players[:team_len:]
second_team = list_players[team_len::]
print(first_team)
print(second_team)
