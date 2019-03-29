import config
from main_page import main_page

hello = f'Добро пожаловать в онлайн-магазин "{config.MARKET_NAME}"'
print('-'*len(hello))
print(f'*# {hello} #*')
print('-'*(len(hello)+6))

main_page()
