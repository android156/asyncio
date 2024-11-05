import asyncio

# Время доставки до разных городов:
delivery_times = {
    'Москва': 1,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 4,
    'Челябинск': 6,
    'Омск': 7,
    'Красноярск': 8,
    'Владивосток': 9,
    'Хабаровск': 9
}


# Заказы:
# orders = [(подарок, город, пометка), ...]
orders = [
    ('Набор для выпечки', 'Санкт-Петербург', 'важно'),
    ('Магнит на холодильник', 'Новосибирск', 'нет'),
    ('Пазл', 'Екатеринбург', 'нет'),
    ('Настольная игра', 'Нижний Новгород', 'нет'),
    ('Новогодняя шапка', 'Челябинск', 'важно'),
    ('Брелок', 'Омск', 'нет')]

# Время до нового года:
# days_left =
days_left = 3

# Тут пишите ваш код:
async def deliver(order):
    delivery_time = delivery_times[order[1]]
    await asyncio.sleep(delivery_time)
    print(f'Подарок {order[0]} успешно доставлен в {order[1]}')


async def main(days_left):
    shielded_and_usual_tasks = []
    for order in orders:
        if order[2] == 'важно':
            task = asyncio.shield(deliver(order))
        else:
            task = asyncio.create_task(deliver(order))
        shielded_and_usual_tasks.append(task)

    # Получаем список всех задач в цикле событий кроме задачи, созданной из main()
    tasks = [task for task in asyncio.all_tasks() if task.get_name() != 'Task-1']

    # Отправляем все, что успеваем, остальное попытаемся отменить
    done, pending = await asyncio.wait(shielded_and_usual_tasks, timeout=days_left)
    [future.cancel() for future in pending]

    for task in tasks:
        try:
            result = await task
        except asyncio.CancelledError as ex:
            pass

asyncio.run(main(days_left))