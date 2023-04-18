"""
Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными.
Для этого: Создать функцию write_order_to_json(), в которую передается 5 параметров —
товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра. 
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    """Запись в json"""

    with open('data/orders.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open('data/orders.json', 'w', encoding='utf-8', ) as f:
        order_info = {'item': item,
                    'quantity': quantity,
                    'price': price,
                    'buyer': buyer,
                    'date': date}
        data['orders'].append(order_info)
        json.dump(data, f, indent=4, ensure_ascii=False)


write_order_to_json('Видеокарта', '1', '68999', 'Аноним', '18.04.2022')
write_order_to_json('Процессор', '1', '25999', 'Аноним', '18.04.2022')
write_order_to_json('Мат. плата', '1', '12999', 'Аноним', '18.04.2022')
write_order_to_json('SSD', '2', '16999', 'Аноним', '18.04.2022')
