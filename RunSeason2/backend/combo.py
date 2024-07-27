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
                if not basket_products:
                    can_buy_combo = True
        else:
            break

    for product in basket_products:
        total_cost += basket_products[product] * products[product]
    total_cost += combo_count * combo_price
    print(total_cost)

if __name__ == '__main__':
    optimize_summ()
