from pprint import pprint


def create_struct_from_file():
    cook_book = dict()
    with open("recipes.txt", mode='r', encoding='utf-8') as recipes_file:
        for line in recipes_file:
            one_line = line.rstrip()
            if one_line == '':
                continue
            if len(one_line.split('|')) == 1 and not one_line.isdigit():
                cook_book.update({one_line: []})
                cook_key = one_line
            if len(one_line.split('|')) == 3:
                ingredient_list = one_line.split('|')
                cook_book[cook_key].append({'ingredient_name': ingredient_list[0].strip(), 'quantity': int(ingredient_list[1]), 'measure': f'{ingredient_list[2].strip()}.'})
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = dict()
    for dish in dishes:
        try:
            ingredient_list = cook_book[dish.capitalize()]
        except KeyError:
            print(f"Блюда '{dish.capitalize()}' нет в списке! Полный список блюд: {list(cook_book.keys())}")
            return None

        for ingredient in ingredient_list:
            try:
                shop_list[ingredient['ingredient_name']]
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                            'quantity': shop_list[ingredient['ingredient_name']][
                                                                            'quantity'] +
                                                                        ingredient['quantity'] * person_count}
            except KeyError:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                            'quantity': ingredient['quantity'] * person_count}
    return shop_list


def input_data():
    input_flag = True
    dish_verify = bool
    print("Доступные блюда:")
    print("-" * 25)
    [print(x) for x in cook_book.keys()]
    print("-" * 25)
    while input_flag:
        in_dish = input("Введите название блюд через запятую (омлет,утка по-пекински,... и т.д): ").split(',')
        for i in in_dish:
            if i.capitalize() not in cook_book.keys():
                print(f"Блюда '{i.capitalize()}' нет в списке!")
                dish_verify = False
                break
            else:
                dish_verify = True
        while dish_verify:
            in_person = int(input("Введите количество персон: "))
            if in_person < 1:
                print(f"Людей не может быть {in_person}")
                continue
            else:
                input_flag = False
                dish_verify = False

        print("-" * 25)
    return in_dish, in_person


if __name__ == '__main__':
    cook_book = create_struct_from_file()
    dish, person = input_data()
    dishes_list = get_shop_list_by_dishes(dish, person)
    if dishes_list is not None:
        pprint(dishes_list)
