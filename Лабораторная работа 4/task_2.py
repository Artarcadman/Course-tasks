# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # Десериалзация из CSV файла
    with open(INPUT_FILENAME) as csv_file:
        csv_data = [line for line in csv.DictReader(csv_file)]
    # Сериализция в JSON файл с отступами равными 4
        with open(OUTPUT_FILENAME, "w") as json_file:
            json.dump(csv_data, json_file, indent = 4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
