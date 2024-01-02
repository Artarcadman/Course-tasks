# TODO Напишите функцию для поиска индекса товара
def find_item_in_list(items_list, find_item):
    if find_item in items_list:
        index_of_item = items_list.index(find_item)
        return index_of_item
    else:
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_in_list(items_list,find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
