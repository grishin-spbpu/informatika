# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as f: #Открываем входной файл в режиме чтения. with автоматически
                                    #закроет файл после выполнения кода
        lines = [line for line in csv.DictReader(f)]
        #csv.DictReader читает CSV и превращает каждую строку в словарь
        #Ключи словаря - названия столбцов, значения - данные строки
        #[line for line in csv.DictReader(f)]:
        #   Проходит по всем строкам CSV и собирает их в список
        #   Каждый элемент списка - это словарь вида {столбец: значение}
    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w") as f: #Открываем выходной JSON файл в режиме записи файл
                                          #будет создан или перезаписан если существует
        json.dump(lines, f, indent = 4)
        #json.dump() - сериализует Python объект в JSON и записывает в файл
        #Аргументы:
        #   lines - данные для сериализации (список словарей)
        #   f - файловый объект, куда записываем
        #   indent = 4 - добавляет отступы в 4 пробела


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
