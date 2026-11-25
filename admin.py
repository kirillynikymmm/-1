import model
import view


def run_admin():
    password = view.ask_choice("Введите пароль от админки (1234): ")
    if password != "1234":
        view.show_error("Неправильный пароль")
        return

    while True:
        view.show_admin_menu()
        choice = view.ask_choice()

        if choice == "1":
            view.show_status(model.get_status(), model.DRINKS_MENU)

        elif choice == "2":
            view.show_orders_history(model.robot_state["orders_history"])

        elif choice == "3":
            for item in model.robot_state["ingredients"]:
                model.robot_state["ingredients"][item] = 10
            for num in model.DRINKS_MENU:
                model.DRINKS_MENU[num]["stock"] = 10
            view.show_message("Все продукты пополнены до 10!")

        elif choice == "4":
            name = view.ask_choice("Название нового ингредиента: ").capitalize()
            if name == "":
                view.show_error("Пустое название")
                continue
            count = view.ask_number("Сколько штук добавить? ", 1, 100)
            if name in model.robot_state["ingredients"]:
                model.robot_state["ingredients"][name] = model.robot_state["ingredients"][name] + count
            else:
                model.robot_state["ingredients"][name] = count
            view.show_message(f"Добавлено: {name} ({count} шт.)")

        elif choice == "5":
            name = view.ask_choice("Название новой пиццы: ")
            toppings = view.ask_custom_toppings(model.get_available_toppings())
            if name == "" or len(toppings) == 0:
                view.show_error("Нужно название и хотя бы 1 начинка!")
                continue
            new_num = str(len(model.PIZZA_MENU) + 1)
            model.PIZZA_MENU[new_num] = {"name": name, "ingredients": toppings}
            view.show_message(f"Пицца '{name}' добавлена под номером {new_num}!")

        elif choice == "6":
            name = view.ask_choice("Название нового напитка: ")
            min_age = view.ask_number("С какого возраста можно? (0 - всем, 18 - взрослым): ", 0, 18)
            stock = view.ask_number("Сколько штук на складе? ", 1, 100)
            new_num = str(len(model.DRINKS_MENU) + 1)
            model.DRINKS_MENU[new_num] = {"name": name, "min_age": min_age, "stock": stock}
            view.show_message(f"Напиток '{name}' добавлен под номером {new_num}!")

        elif choice == "0":
            break
        else:
            view.show_error("Нет такой команды")
