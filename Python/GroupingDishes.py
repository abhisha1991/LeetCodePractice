# https://codefights.com/interview-practice/task/xrFgR63cw7Nch4vXo
from collections import defaultdict


def groupingDishes(dishes):
    all_ingredients_with_dishes = defaultdict(list)
    for d in dishes:
        dish = d[0]
        ingredients = d[1:]
        for i in ingredients:
            all_ingredients_with_dishes[i].append(dish)

    result = []
    for key in all_ingredients_with_dishes.keys():
        if len(all_ingredients_with_dishes[key]) < 2:
            continue
        else:
            inner_result = sorted(all_ingredients_with_dishes[key])
            inner_result = [key] + inner_result
            row = 0
            for r in result:
                if key > r[0]:
                    row += 1

            result.insert(row, inner_result)

    return result


groupingDishes([["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]])