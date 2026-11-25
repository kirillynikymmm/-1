import asyncio
import model


async def bake_one_pizza(oven_number, pizza_name, ingredients):
    print(f"[Печь №{oven_number}] Разогрев ......Выпекаем '{pizza_name}'")
    await asyncio.sleep(3)
    model.robot_state["orders_completed"] = model.robot_state["orders_completed"] + 1
    print(f"[Печь №{oven_number}] Готово Пицца '{pizza_name}' ({', '.join(ingredients)})")


async def bake_all_pizzas(pizzas_list):
    tasks = []
    oven_num = 1

    for pizza in pizzas_list:
        name = pizza[0]
        ingr = pizza[1]
        task = asyncio.create_task(bake_one_pizza(oven_num, name, ingr))
        tasks.append(task)

        if oven_num == 1:
            oven_num = 2
        else:
            oven_num = 1

    await asyncio.gather(*tasks)
