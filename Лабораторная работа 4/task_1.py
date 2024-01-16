import json

INPUT_FILE = "input.json"

def task() -> float:
    """ Функция для нахождения суммы произведений значений словаря"""
    with open(INPUT_FILE) as json_file:
        json_data = json.load(json_file)
        sum_of_values = sum(value["score"] * value["weight"] for value in json_data)
    return round(sum_of_values,3)
print(task())
