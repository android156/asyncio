import asyncio


async def coro():
    name = asyncio.current_task().get_name()
    print(f'{name} начала свою работу!')
    await asyncio.sleep(1)
    print(f'{name} завершена!')


async def ex_coro():
    await asyncio.sleep(.5)
    # Вызываем исключение
    print('ex_coro поднимает исключение Exсeption')
    raise Exception('Что-то пошло не так!(((')


async def main():
    try:
        # Создание группы задач
        async with asyncio.TaskGroup() as group:
            # Создание трех задач
            tasks = [group.create_task(coro(), name=f'Задача_0{i}') for i in range(1, 4)]
            # Создание задачи, имитирующей возникновение исключения
            tasks.append(group.create_task(ex_coro(), name='Задача_ex'))
    except:
        pass

    # Проверка состояния каждой задачи
    for task in tasks:
        print(f'{task.get_name()}: done={task.done()}, cancelled={task.cancelled()}')
    print(f'{task.get_name()}: {tasks[-1].exception()}')


asyncio.run(main())