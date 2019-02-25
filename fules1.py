with open('test.txt') as recipies:
    while True:
        ingridient_list = []
        ingr_dicts_list = []
        name = recipies.readline().strip()
        cook_book = {name:ingr_dicts_list}
        if not name:
            break
        ingr_num = int(recipies.readline().strip())
        for i in range(0,ingr_num):
            ingridient_list.append(recipies.readline().strip())
        recipies.readline()
        for ingridient in ingridient_list:
           one_ingr_list = ingridient.split('|')
           ingr_dict = dict(ingridient_name=one_ingr_list[0], quantity=one_ingr_list[1], measure=one_ingr_list[2])
           ingr_dicts_list.append(ingr_dict)
        print(cook_book)
def get_shop_list_by_dishes(dishes = [], person_count = int(input("Введите количество персон: "))):
    dishes_num = int(input("Количество блюд:"))
    for i in range(0,dishes_num):
        dish = input("Введите блюдо: ")
        dishes.append(dish)
    needed_list = []
    for dish, ingridients in cook_book.items():
        if dish in dishes:
            for ingridient in ingridients:
                needed_num = ingridient.get(quantity)
                needed_num *= person_count
                one_ingr_dict = {quantity:needed_num,measure:ingridient.get(measure)}
                needed_list.append(one_ingr_dict)
                shop_list = {ingridient.get(ingridient_name):needed_list}
                return shop_list
print(get_shop_list_by_dishes())
            

        
