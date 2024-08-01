'''
def optimize_summ():
    n = int(input())
    price_list = list(map(int, input().split()))
    combo_price = int(input())
    combo_list = list(map(int, input().split()))
    basket_cnt = int(input())
    basket_list = list(map(int, input().split()))

    products = {}
    for i in range(n):
        product_id = i + 1
        products[product_id] = price_list[i]

    basket_products = {}
    for product in basket_list:
        if product in basket_products:
            basket_products[product] += 1
        else:
            basket_products[product] = 1

    combo_products = {}
    for product in combo_list:
        if product in combo_products:
            combo_products[product] += 1
        else:
            combo_products[product] = 1

    total_cost = 0
    combo_count = 0

    while True:
        can_buy_combo = True
        for product in combo_products:
            if product not in basket_products:
                can_buy_combo = False
                break
        if can_buy_combo:
            combo_count += 1
            for product in combo_products:
                basket_products[product] -= combo_products[product]
                if len(basket_products) >= 0:
                    can_buy_combo = True
                    break
        else:
            break

    for product in basket_products:
        total_cost += basket_products[product] * products[product]
    total_cost += combo_count * combo_price
    print(total_cost)

if __name__ == '__main__':
    optimize_summ()
'''

def optimize_summ():
    n = int(input())
    price_list = list(map(int, input().split()))
    combo_price = int(input())
    combo_list = list(map(int, input().split()))
    basket_cnt = int(input())
    basket_list = list(map(int, input().split()))

    products = {i + 1: price_list[i] for i in range(n)}

    basket_products = {}
    for product in basket_list:
        if product in basket_products:
            basket_products[product] += 1
        else:
            basket_products[product] = 1

    total_cost = 0

    while True:
        can_buy_combo = any(basket_products.get(product, 0) > 0 for
            product in combo_list)

        if can_buy_combo:
            combo_count = min(basket_products[product] for
                product in combo_list if basket_products.get(product, 0) > 0)
            separate_cost = sum(products[product] for product in combo_list)

            if combo_price < separate_cost:
                total_cost += combo_count * combo_price
                for product in combo_list:
                    if product in basket_products:
                        basket_products[product] -= combo_count
            else:
                break
        else:
            break

    for product in basket_products:
        if basket_products[product] > 0:
            total_cost += basket_products[product] * products[product]

    for product in combo_list:
        if basket_products.get(product, 0) > 0:
            # Считаем, сколько раз можно купить комбо для оставшихся товаров
            remaining_combo_count = min(basket_products[product] for product in combo_list if basket_products.get(product, 0) > 0)

            # Сравниваем стоимость оставшихся товаров с комбо
            if combo_price < sum(products[prod] for prod in combo_list):
                total_cost += remaining_combo_count * combo_price
                for prod in combo_list:
                    if prod in basket_products:
                        basket_products[prod] -= remaining_combo_count

    # Подсчитываем стоимость оставшихся товаров после всех покупок
    for product in basket_products:
        if basket_products[product] > 0:
            total_cost += basket_products[product] * products[product]

    print(total_cost)

if __name__ == '__main__':
    optimize_summ()

'''
Решение прошло 3 теста из 9

def optimize_summ():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    price_list = list(map(int, data[1:n+1]))
    combo_price = int(data[n+1])
    combo_list = list(map(int, data[n+2:n+6]))
    k = int(data[n+6])
    basket_list = list(map(int, data[n+7:]))

    # Цены товаров
    products = {i + 1: price_list[i] for i in range(n)}

    # Количество товаров в корзине
    basket_products = {}
    for product in basket_list:
        if product in basket_products:
            basket_products[product] += 1
        else:
            basket_products[product] = 1

    # Количество товаров в комбо
    combo_products = {product: combo_list.count(product) for product in combo_list}

    total_cost = 0

    # Сначала покупаем максимально возможное количество комбо
    while all(basket_products.get(product, 0) >= combo_products[product] for product in combo_products):
        total_cost += combo_price
        for product in combo_products:
            basket_products[product] -= combo_products[product]

    # Подсчитываем остаточную стоимость
    remaining_cost = 0
    for product, count in basket_products.items():
        if count > 0:
            remaining_cost += count * products[product]

    # Проверяем, можно ли частично использовать комбо для оставшихся товаров
    if remaining_cost > combo_price:
        total_cost += combo_price
    else:
        total_cost += remaining_cost

    # Оптимизация для частичного использования комбо
    combo_remainder = combo_list[:]
    for product in basket_products:
        while basket_products[product] > 0 and combo_remainder:
            if product in combo_remainder:
                combo_remainder.remove(product)
                basket_products[product] -= 1
                remaining_cost -= products[product]
            else:
                break

    if remaining_cost > combo_price:
        total_cost += combo_price
    else:
        total_cost += remaining_cost

    print(total_cost)

if __name__ == '__main__':
    optimize_summ()
'''
