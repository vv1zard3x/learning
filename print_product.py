def print_product(product):
    print('*'*10)
    print(product['name'])
    print(f"Цена: {product['price']} рублей")
    if 'firm' in product:
        print(f"Производитель: {product['firm']}")
    if product['description'] != '':
        print(f'Описание: {product["description"]}')
    print('')
    print('')
