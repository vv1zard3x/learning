import print_products
from products import products_list
from find_product import find_product, find_many_category, find_firm
import config


def main_page():
    print("Что вы хотите?\n1.Открыть каталог\n2.Поиск по сайту")
    try:
        a = int(input('==>> '))
        if a == 1:
            print("1. Показать все товары\n2. Категории\n3. Производитель")
            request = int(input())
            if request == 1:
                print_products.print_products(products_list)
            elif request == 2:
                print(f'Выберите категорию:\n1.Наушники\n2.Ноутбуки\n'
                      f'3.Телефоны\n4.Аксесуары\n5.Мыши\n6.Клавиатуры')
                category = int(input('==>> '))
                if category == 1:
                    print('1.Показать все\n2.Проводные\n3.Беспроводные\n4.Игровые')
                    subcutegory = int(input('==>> '))
                    if subcutegory == 1:
                        pr_list = find_many_category(products_list, 'наушники')
                        print_products.print_products(pr_list)
                    elif subcutegory == 2:
                        pr_list = find_many_category(products_list, 'наушники', 'проводные')
                        print_products.print_products(pr_list)
                    elif subcutegory == 3:
                        pr_list = find_many_category(products_list, 'наушники', 'беспроводные')
                        print_products.print_products(pr_list)
                    elif subcutegory == 4:
                        pr_list = find_many_category(products_list, 'наушники', 'игровые')
                        print_products.print_products(pr_list)
                    else:
                        print(config.USER_DIAGNOSIS)
                elif category == 2:
                    print('1.Показать все\n2.Игровые\n3.Ультрабуки')
                    subcutegory = int(input())
                    if subcutegory == 1:
                        print_products.print_products(find_many_category(products_list, 'ноутбуки'))
                    elif subcutegory == 2:
                        print_products.print_products(find_many_category(products_list, 'ноутбуки', 'игровые'))
                    elif subcutegory == 3:
                        print_products.print_products(find_many_category(products_list, 'ноутбуки', 'ультрабуки'))
                    else:
                        print_products.print_products(config.USER_DIAGNOSIS)
                elif category == 3:
                    print('1.Показать все\n2.Кнопочные\n3.Неубиваемые\n4.Смартфоны')
                    subcutegory = int(input())
                    if subcutegory == 1:
                        print_products.print_products(find_many_category(products_list, 'телефоны'))
                    elif subcutegory == 2:
                        print_products.print_products(find_many_category(products_list, 'телефоны', 'кнопочные'))
                    elif subcutegory == 3:
                        print_products.print_products(find_many_category(products_list, 'телефоны', 'неубиваемые'))
                    elif subcutegory == 4:
                        print_products.print_products(find_many_category(products_list, 'телефоны', 'смартфоны'))
                    else:
                        print_products.print_products(config.USER_DIAGNOSIS)
                elif category == 4:
                    print('1.Показать все')
                    subcutegory = int(input())
                    if subcutegory == 1:
                        print_products.print_products(find_many_category(products_list, 'аксесуары'))
                    else:
                        print_products.print_products(config.USER_DIAGNOSIS)
                elif category == 5:
                    print('1.Показать все\n2.Игровые\n3.Проводные\n4.Беспроводные')
                    subcutegory = int(input())
                    if subcutegory == 1:
                        print_products.print_products(find_many_category(products_list, 'мыши'))
                    elif subcutegory == 2:
                        print_products.print_products(find_many_category(products_list, 'мыши', 'игровые'))
                    elif subcutegory == 3:
                        print_products.print_products(find_many_category(products_list, 'мыши', 'проводные'))
                    elif subcutegory == 4:
                        print_products.print_products(find_many_category(products_list, 'мыши', 'беспроводные'))
                    else:
                        print_products.print_products(config.USER_DIAGNOSIS)
                elif category == 6:
                    print('1.Показать все\n2.Игровые\n3.Проводные\n4.Беспроводные')
                    subcutegory = int(input())
                    if subcutegory == 1:
                        print_products.print_products(find_many_category(products_list, 'клавиатуры'))
                    elif subcutegory == 2:
                        print_products.print_products(find_many_category(products_list, 'клавиатуры', 'игровые'))
                    elif subcutegory == 3:
                        print_products.print_products(find_many_category(products_list, 'клавиатуры', 'проводные'))
                    elif subcutegory == 4:
                        print_products.print_products(find_many_category(products_list, 'клавиатуры', 'беспроводные'))
                    else:
                        print_products.print_products(config.USER_DIAGNOSIS)
            elif request == 3:
                print(f'Выберите фирму:\n1.Acer\n2.Apple\n3.Nokia\n4.Bloody\n'
                      f'5.Razer\n6.Sony\n7.Logitech\n8.Genius\n9.Meizu')
                firm_input = int(input())
                if firm_input == 1:
                    find_firm('acer', products_list)
                elif firm_input == 2:
                    find_firm('apple', products_list)
                elif firm_input == 3:
                    find_firm('nokia', products_list)
                elif firm_input == 4:
                    find_firm('bloody', products_list)
                elif firm_input == 5:
                    find_firm('razer', products_list)
                elif firm_input == 6:
                    find_firm('sony', products_list)
                elif firm_input == 7:
                    find_firm('logitech', products_list)
                elif firm_input == 8:
                    find_firm('genius', products_list)
                elif firm_input == 9:
                    find_firm('meizu', products_list)
                else:
                    print(config.USER_DIAGNOSIS)
            else:
                print(config.USER_DIAGNOSIS)
        elif a == 2:
            print('Что искать?')
            request = input('==>> ')
            print(f'Товары по запросу {request}:')
            find_product(request, products_list)
        else:
            print(config.USER_DIAGNOSIS)
    except ValueError:
        print(config.USER_DIAGNOSIS)
