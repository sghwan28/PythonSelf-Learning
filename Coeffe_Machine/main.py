from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice.lower() == "off":
        is_on = False
    elif choice.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice.lower() == 'service':
        pass
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)


'''
一些可供修改的点：
1. 在机器检测到硬币已经足够时，不再投币
2. 当机器内原料不足时，不再提出收费，而是返回menu界面并提示原料不足
3. Service mode, 在此模式下可以取出机器内钱币或者为机器添加原材料
'''