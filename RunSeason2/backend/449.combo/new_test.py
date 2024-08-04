def find_optimal_cost(cnt_products, products_prices, comb_price, product_list, products_counter, basket_list):
    products = {i+1: products_prices[i] for i in range(cnt_products)}
    basket_products = {product: basket_list.count(product) for product in set(basket_list)}
    combo_products = {product: product_list.count(product) for product in set(product_list)}

    total_cost = 0
    extra_products = []

    while any(value > 0 for value in basket_products.values()):
        # Проверяем, можем ли мы собрать комбо из текущих товаров в корзине
        can_buy_combo = True
        for product, count in combo_products.items():
            if basket_products.get(product, 0) < count:
                can_buy_combo = False
                break

        if can_buy_combo:
            # Если можем купить комбо, уменьшаем количество продуктов в корзине и добавляем стоимость комбо
            for product, count in combo_products.items():
                basket_products[product] -= count
                extra_products.append(product)
            total_cost += comb_price
        else:
            # Если не можем купить комбо, находим наиболее дешевый вариант среди оставшихся товаров
            min_cost = float('inf')
            min_product = None
            for product, count in basket_products.items():
                if count > 0 and products[product] < min_cost:
                    min_cost = products[product]
                    min_product = product

            # Уменьшаем количество этого товара в корзине и добавляем его стоимость к общей стоимости
            if min_product:
                basket_products[min_product] -= 1
                total_cost += products[min_product]

    # Используем лишние товары для покупки комбо или отдельных товаров
    while extra_products:
        # Проверяем, можем ли мы собрать комбо из текущих лишних товаров
        can_buy_combo = True
        for product, count in combo_products.items():
            if extra_products.count(product) < count:
                can_buy_combo = False
                break

        if can_buy_combo:
            # Если можем купить комбо, уменьшаем количество лишних товаров и добавляем стоимость комбо
            for product in product_list:
                while extra_products.count(product) >= combo_products[product]:
                    extra_products.remove(product)
            total_cost += comb_price
        else:
            # Если не можем купить комбо, находим наиболее дешевый вариант среди оставшихся лишних товаров
            min_cost = float('inf')
            min_product = None
            for product in set(extra_products):
                if products[product] < min_cost:
                    min_cost = products[product]
                    min_product = product

            # Удаляем один экземпляр этого товара из лишних товаров и добавляем его стоимость к общей стоимости
            if min_product:
                extra_products.remove(min_product)
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
