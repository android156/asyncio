import asyncio


async def coro(value):
    await asyncio.sleep(1)
    return value * 100


async def main():
    # Создание группы задач
    async with asyncio.TaskGroup() as group:
        # Создание списка задач с передачей в них чисел из диапазона (1, 10)
        tasks = [group.create_task(coro(i)) for i in range(1, 11)]

    for task in tasks:
        print(task.result())


asyncio.run(main())