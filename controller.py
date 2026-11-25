import model
import view
import oven
import admin


async def handle_order():
    ages = view.ask_company_ages()
    pizzas_to_bake = []
    drinks_list = []

    person_num = 1
    for age in ages:
        print(f"\n=== Заказ для {person_num}-го человека (возраст: {age}) ===")

        view.show_pizza_menu(model.PIZZA_MENU)
        p_choice = view.ask_choice("Номер пиццы: ")

        if p_choice in model.PIZZA_MENU:
            pizza = model.PIZZA_MENU[p_choice]
            ok, result = model.check_and_use_ingredients(pizza["ingredients"])
            if ok:
                pizzas_to_bake.append([pizza["name"], result])
                view.show_message(f"Пицца '{pizza['name']}' принята!")
            else:
                view.show_error(result)

        elif p_choice == "11":
            toppings = view.ask_custom_toppings(model.get_available_toppings())
            ok, result = model.check_and_use_ingredients(toppings)
            if ok:
                pizzas_to_bake.append(["Своя пицца", result])
                view.show_message("Своя пицца принята!")
            else:
                view.show_error(result)

        elif p_choice == "0":
            view.show_message("Пиццу пропустили.")
        else:
            view.show_error("Нет такой пиццы.")

        view.show_drinks_menu(model.DRINKS_MENU, age)
        d_choice = view.ask_choice("Номер напитка: ")
        if d_choice != "0":
            ok, drink_name = model.take_drink(d_choice, age)
            if ok:
                drinks_list.append(f"{person_num}-й человек: {drink_name}")
                view.show_message(f"Выбран напиток: {drink_name}")
            else:
                view.show_error(drink_name)

        person_num = person_num + 1

    if len(pizzas_to_bake) > 0:
        view.show_message("\nОтправляем пиццы в печи...")
        model.robot_state["status"] = "Готовит заказ"
        await oven.bake_all_pizzas(pizzas_to_bake)
        model.robot_state["status"] = "Ожидает заказ"

    if len(pizzas_to_bake) > 0 or len(drinks_list) > 0:
        pizza_names = []
        for p in pizzas_to_bake:
            pizza_names.append(p[0])

        order_info = {
            "people_count": len(ages),
            "pizzas": pizza_names,
            "drinks": drinks_list
        }
        model.robot_state["orders_history"].append(order_info)

        print("\n=== ВАШ ЗАКАЗ ГОТОВ ===")
        for p in pizzas_to_bake:
            print("- Пицца:", p[0])
        for d in drinks_list:
            print("- Напиток:", d)
        print("Приятного аппетита!")


async def run_robot():
    view.show_welcome()

    while True:
        view.show_main_menu()
        choice = view.ask_choice()

        if choice == "1":
            await handle_order()
        elif choice == "2":
            admin.run_admin()
        elif choice == "0":
            view.show_message("Выключение системы")
            break
        else:
            view.show_error("Неизвестная команда")
