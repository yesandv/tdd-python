def split_list(general_list):
    list_of_dishes_and_prices = []
    for item in general_list:
        dish = item.split()[0]
        price = int(item.split()[1])
        list_of_dishes_and_prices.append(dish)
        list_of_dishes_and_prices.append(price)
    return list_of_dishes_and_prices


def split_list_to_list_of_tuples(dish_price_list):
    list_of_tuples = []
    dishes = dish_price_list[0:len(dish_price_list):2]
    prices = dish_price_list[1:len(dish_price_list):2]
    for i in range(0, len(dishes)):
        dish_price = (dishes[i], prices[i])
        list_of_tuples.append(dish_price)
    return list_of_tuples


def calculate_min_sum_of_losses(list_of_tuples):
    min_sum = 0
    for i in range(0, len(list_of_tuples), 2):
        price_1 = list_of_tuples[i][1]
        price_2 = list_of_tuples[i + 1][1]
        if price_1 >= price_2:
            min_sum += price_2
        else:
            min_sum += price_1
    if len(list_of_tuples) < 20:
        min_sum += 20000
    return min_sum


if __name__ == "__main__":
    general_list = []
    number_of_orders = int(input("Укажите кол-во блюд: "))
    for k in range(number_of_orders):
        dish_price_1 = input("Введите первое блюдо и его цену: ")
        dish_price_2 = input("Введите второе блюдо и его цену: ")
        general_list.append(dish_price_1)
        general_list.append(dish_price_2)
    dish_price_list = split_list(general_list)
    dish_price_tuples = split_list_to_list_of_tuples(dish_price_list)
    min_sum = calculate_min_sum_of_losses(dish_price_tuples)
    print(min_sum)
