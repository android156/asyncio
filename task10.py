import asyncio


async def simulate_long_running_task(name, delay, future: asyncio.Future):
    print(f"Задача '{name}' началась, будет выполнена за {delay} секунд.")
    await asyncio.sleep(delay)
    result = f"Результат задачи '{name}'"
    print(f"Задача '{name}' завершена.")
    future.set_result(result)  # Устанавливаем результат для Future объекта


async def main():
    # Создаем объект Future
    future = asyncio.Future()

    # Запускаем корутину, передаем Future объект в функцию
    await simulate_long_running_task("Задача1", 1, future)

    # Получаем результат выполнения задачи
    result = future.result()
    print(f"Результат Future: {result}")


asyncio.run(main())