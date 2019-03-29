from print_product import print_product


def find_product(request, products_list):
    for product in products_list:
        products = f"{product['name']} {product['firm']} {product['description']}"
        if request.upper() in products.upper():
            print_product(product)


def find_firm(request, products_list):
    for product in products_list:
        products = product['firm'].upper()
        if request.upper() in products:
            print_product(product)


def find_many_category(products_list, category1, category2='', category3='', category4=''):
    list_prod = []
    list_prod1 = []
    list_prod2 = []
    list_prod3 = []
    for product in products_list:
        products = [x.upper() for x in product['category']]
        if category1.upper() in products:
            list_prod.append(product)
    for product in list_prod:
        products = [x.upper() for x in product['category']]
        if category2.upper() in products:
            list_prod1.append(product)
    for product in list_prod1:
        products = [x.upper() for x in product['category']]
        if category3.upper() in products:
            list_prod2.append(product)
    for product in list_prod2:
        products = [x.upper() for x in product['category']]
        if category4.upper() in products:
            list_prod3.append(product)
    if category4 != '':
        return list_prod3
    elif category3 != '':
        return list_prod2
    elif category2 != '':
        return list_prod1
    else:
        return list_prod
