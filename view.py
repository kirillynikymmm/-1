def decor_func(input_func):
    def outer_func():
        print("*" * 30)
        input_func()
        print("*" * 30)
    return outer_func


@decor_func
def show_welcome():
    print("Робот пицца мейкер запущен")


def show_main_menu():
    print("\nВыберите действие:")
    print("1. Сделать заказ")
    print("2. Админка")
    print("0. Выключить робота")


def ask_choice(text="Ваш выбор: "):
    return input(text).strip()


def ask_number(text, min_num, max_num):
    while True:
        ans = input(text).strip()
        if ans.isdigit():
            num = int(ans)
            if num >= min_num and num <= max_num:
                return num
        show_error(f"Введите число от {min_num} до {max_num}")


def ask_company_ages():
    print("\nВы один или компанией?")
    print("1. Один")
    print("2. Компанией")
    ans = ask_choice("Ваш выбор (1 или 2): ")

    ages = []
    if ans == "1":
        age = ask_number("Сколько вам лет? ", 1, 120)
        ages.append(age)
    elif ans == "2":
        people = ask_number("Сколько вас человек? ", 2, 20)
        for i in range(1, people + 1):
            age = ask_number(f"Возраст {i}-го человека: ", 1, 120)
            ages.append(age)
    else:
        show_error("Не понял выбор, пусть будет 1 человек")
        age = ask_number("Сколько вам лет? ", 1, 120)
        ages.append(age)

    return ages


def show_pizza_menu(pizza_menu):
    print("\n--- МЕНЮ ПИЦЦ ---")
    for num in pizza_menu:
        name = pizza_menu[num]["name"]
        ingr = ", ".join(pizza_menu[num]["ingredients"])
        print(f"{num}. {name} ({ingr})")
    print("11. Собрать свою пиццу")
    print("0. Не брать пиццу")


def ask_custom_toppings(toppings_list):
    print("\nВЫБЕРИТЕ НАЧИНКИ")
    for i in range(len(toppings_list)):
        print(f"{i + 1}. {toppings_list[i]}")

    print("Напишите номера через запятую (например: 1, 3) или 0:")
    raw = input("> ").strip()
    if raw == "" or raw == "0":
        return []

    chosen = []
    parts = raw.split(",")
    for part in parts:
        part = part.strip()
        if part.isdigit():
            index = int(part) - 1
            if index >= 0 and index < len(toppings_list):
                chosen.append(toppings_list[index])
    return chosen


def show_drinks_menu(drinks_menu, age):
    print(f"\nНАПИТКИ (ваш возраст: {age}) ")
    for num in drinks_menu:
        drink = drinks_menu[num]
        if drink["min_age"] >= 18 and age < 18:
            print(f"{num}. 18+")
        else:
            print(f"{num}. {drink['name']} (осталось {drink['stock']} шт.)")
    print("0. Без напитка")


def show_status(state, drinks_menu):
    print("*" * 30)
    print(f"Статус: {state['status']}")
    print(f"Приготовлено пицц: {state['orders_completed']}")
    print("\nИнгредиенты на складе:")
    for item in state["ingredients"]:
        print(f"- {item}: {state['ingredients'][item]} шт.")
    print("\nНапитки на складе:")
    for num in drinks_menu:
        d = drinks_menu[num]
        print(f"- {d['name']} ({d['min_age']}+): {d['stock']} шт.")
    print("*" * 30)


def show_orders_history(history):
    print("\n=== ИСТОРИЯ ВСЕХ ЗАКАЗОВ ===")
    if len(history) == 0:
        print("Заказов пока не было.")
        return

    for i in range(len(history)):
        order = history[i]
        print(f"\nЗаказ №{i + 1} (человек в заказе: {order['people_count']}):")
        if len(order["pizzas"]) > 0:
            print("  Пиццы:", ", ".join(order["pizzas"]))
        else:
            print("  Пиццы: нет")

        if len(order["drinks"]) > 0:
            print("  Напитки:", ", ".join(order["drinks"]))
        else:
            print("  Напитки: нет")


def show_admin_menu():
    print("\n--- АДМИНКА ---")
    print("1. Посмотреть статус и остатки на складе")
    print("2. Посмотреть список всех заказов")
    print("3. Пополнить все запасы до 10")
    print("4. Добавить новый ингредиент")
    print("5. Добавить новую пиццу в меню")
    print("6. Добавить новый напиток в меню")
    print("0. Выйти в главное меню")


def show_message(msg):
    print(f"[Инфо] {msg}")


def show_error(err):
    print(f"[Ошибка] {err}")
