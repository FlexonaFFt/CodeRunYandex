def find_optimal_cost(cnt_products, products_prices, comb_price, product_list, products_counter, basket_list):

    products = {}
    for i in range(n):
        product_id = i + 1
        products[product_id] = products_prices[i]

    basket_products = {}
    for product in basket_list:
        if product in basket_products:
            basket_products[product] += 1
        else:
            basket_products[product] = 1

    combo_products = {}
    for product in product_list:
        if product in combo_products:
            combo_products[product] += 1
        else:
            combo_products[product] = 1

    total_cost = combo_count = 0

    while any(value > 0 for value in basket_products.values()):

        can_buy_combo = True
        for product, count in combo_products.items():
            if basket_products.get(product, 0) < count:
                can_buy_combo = False
                break

        if can_buy_combo:

            for product, count in combo_products.items():
                basket_products[product] -= count
            total_cost += comb_price
        else:

            min_cost = float('inf')
            min_product = None
            for product, count in basket_products.items():
                if count > 0 and products[product] < min_cost:
                    min_cost = products[product]
                    min_product = product


            if min_product:
                basket_products[min_product] -= 1
                total_cost += products[min_product]

    return total_cost


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    b = list(map(int, input().split()))
    k = int(input())
    c = list(map(int, input().split()))
    print(find_optimal_cost(n, a, x, b, k, c))
