# TODO Напишите функцию find_common_participants
def find_common_participants(first_string, second_string, sep=","):
    #Разделяем строки на списки участников, используя указанный разделитель.
    #.split(sep) разбивает строку на части по разделителю sep
    first_group = first_string.split(sep) #строка с участниками первой группы
    second_group = second_string.split(sep) #строка с участниками второй группы

    final_list = list(set(first_group).intersection(set(second_group))) # Находим пересечение двух
    #списков (общих участников)
    #set(first_group) - преобразуем список в множество (удаляет дубликаты, если они есть)
    #intersection(set(second_group)) - находим элементы, присутствующие в обоих множествах
    #list(...) - преобразуем результат обратно в список

    return sorted(final_list) #Возвращаем отсортированный в алфавитном порядке список общих участников


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print("Общие участники:", find_common_participants(participants_first_group, participants_second_group, "|"))