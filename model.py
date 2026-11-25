robot_state = {
    "status": "Ожидает заказ",
    "ingredients": {
        "Тесто": 10,
        "Соус": 10,
        "Сыр": 10,
        "Пеперони": 8,
        "Грибы": 8,
        "Ветчина": 8,
        "Курица": 8,
        "Ананасы": 6,
        "Бекон": 8,
        "Халапеньо": 6,
        "Томаты": 8,
        "Оливки": 6
    },
    "orders_completed": 0,
    "orders_history": []
}

# Меню из 10 пицц
PIZZA_MENU = {
    "1": {"name": "Маргарита", "ingredients": ["Сыр", "Томаты"]},
    "2": {"name": "Пепперони", "ingredients": ["Сыр", "Пеперони"]},
    "3": {"name": "Гавайская", "ingredients": ["Сыр", "Курица", "Ананасы"]},
    "4": {"name": "Мясная", "ingredients": ["Сыр", "Пеперони", "Ветчина", "Бекон"]},
    "5": {"name": "Грибная", "ingredients": ["Сыр", "Грибы"]},
    "6": {"name": "Дьябло", "ingredients": ["Сыр", "Пеперони", "Халапеньо"]},
    "7": {"name": "Ветчина и грибы", "ingredients": ["Сыр", "Ветчина", "Грибы"]},
    "8": {"name": "Двойной сыр", "ingredients": ["Сыр", "Сыр"]},
    "9": {"name": "Куриная с томатами", "ingredients": ["Сыр", "Курица", "Томаты"]},
    "10": {"name": "Средиземноморская", "ingredients": ["Сыр", "Томаты", "Оливки"]}
}

# Меню напитков
DRINKS_MENU = {
    "1": {"name": "Яблочный сок", "min_age": 0, "stock": 10},
    "2": {"name": "Молочный коктейль", "min_age": 0, "stock": 10},
    "3": {"name": "Кола", "min_age": 6, "stock": 10},
    "4": {"name": "16+", "min_age": 18, "stock": 10},
    "5": {"name": "18+", "min_age": 18, "stock": 10},
    "6": {"name": "18+", "min_age": 18, "stock": 10}
}


def get_status():
    return robot_state.copy()


def get_available_toppings():
    toppings = []
    for item in robot_state["ingredients"]:
        if item != "Тесто" and item != "Соус":
            toppings.append(item)
    return toppings


def check_and_use_ingredients(needed_list):
    inv = robot_state["ingredients"]
    all_items = ["Тесто", "Соус"] + needed_list

    counts = {}
    for item in all_items:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1

    for item in counts:
        if item not in inv or inv[item] < counts[item]:
            return False, f"Не хватает ингредиента: {item}"

    for item in counts:
        inv[item] = inv[item] - counts[item]

    return True, ["Тесто", "Соус"] + needed_list


def take_drink(drink_id, user_age):
    if drink_id not in DRINKS_MENU:
        return False, "Такого напитка нет."

    drink = DRINKS_MENU[drink_id]
    if drink["min_age"] >= 18 and user_age < 18:
        return False, "Нельзя. Этот напиток только 18+."

    if drink["stock"] <= 0:
        return False, "Этот напиток закончился."

    drink["stock"] = drink["stock"] - 1
    return True, drink["name"]
