import asyncio

async def task_func():
    print("Задача 1 запустилась")
    await asyncio.sleep(1)
    print("Задача 1 завершилась")
    return "Результат выполнения задачи 1"

async def another_task_func():
    print("Задача 2 запустилась")
    await asyncio.sleep(2)
    print("Задача 2 завершилась")
    return "Результат выполнения задачи 2"

async def main():
    task1 = asyncio.create_task(task_func())
    task2 = asyncio.create_task(another_task_func())
    print('Первая проверка задачи 1 -', task1.done())
    print('Первая проверка задачи 2 -', task2.done())
    print("Задачи созданы и помещены в стек вызовов")
    await task1
    await task2
    print('Вторая проверка задачи 1 -', task1.done())
    print('Вторая проверка задачи 2 -', task2.done())
    print("Проверка результата задачи 1:", task1.result())
    print("Проверка результата задачи 2:", task2.result())

asyncio.run(main())