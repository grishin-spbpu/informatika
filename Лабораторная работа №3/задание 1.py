# TODO Напишите функцию для поиска индекса товара
def search_first_entry(products_list, desired_product):
    for i in range(len(products_list)): # Перебираем все индексы списка с помощью range, range(len(products_list))
                                        # генерирует числа от 0 до (длины списка - 1)
        if products_list[i] == desired_product: #Если товар с индексом i в списке продуктов является искомым продуктом,
                                                # то возвращаем индекс i. Так как в цикле перебор индексов начинается
                                                # от 0, то в таком случае функция как раз вернёт индекс первого
                                                #вхождения, как того и требует задание
            return i

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search_first_entry(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
