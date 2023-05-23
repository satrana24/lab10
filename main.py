import json


def first():
    with open('1.json', 'r') as file:  # открываем файл для чтения
        data = json.load(file)

    for i in data['products']:
        print('Название товара:', i['name'])
        print('Цена:', i['price'])
        if i['available']:
            print('В наличии')
        else:
            print('Нет в наличии')
        print('Вес:', i['weight'], '\n')


def second():
    count = int(input('Введите количество товаров, которое Вы хотите добавить: '))
    products = {'products': []}
    for i in range(count):
        name = input('Название товара: ')
        price = int(input('Цена: '))
        available = bool(input('Наличие товара (0/1): '))
        weight = int(input('Вес: '))
        products['products'].append({'name': name, 'price': price, 'available': available, 'weight': weight})

    with open('1.json', 'r') as file:
        data = json.load(file)

    data['products'].extend(products['products'])  # добавляем в конец списка введённые продукты и их характеристики

    print('Товар добавлен в список! Нынешний список выглядит так:')

    for i in data['products']:
        print("Название: ", i["name"])
        print("Цена: ", i["price"])
        print("Вес: ", i["weight"])
        print("В наличии" if i["available"] else "Нет в наличии!", "\n")

    with open("1.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)  # 4 отступа, показывает не ASCII символы?


def third():
    d = {}  # пустой словарь, в который всё будем записывать

    with open('en-ru.txt', 'r') as file:
        for line in file:
            en_w = line.split('-')[0].strip()
            ru_ws = line.split('-')[1].strip().split(',')  # strip убирает лишние пробелы между словами
            for i in ru_ws:
                i = i.strip()
                if i in d.keys():  # меняем местами ключ и значение
                    d[i] = d[i] + ", " + en_w  # если два и более перевода
                else:
                    d[i] = en_w  # если один перевод

    with open("ru-en.txt", "w") as file:  # перезаписываем всё в новый файл
        for i in sorted(d.keys()):  # сортируем
            file.writelines(f"{i} - {d[i]}\n")


third()
