import asyncio


async def my_coroutine():
    # Получаем имя текущей задачи.
    task = asyncio.current_task()
    task_name = task.get_name()

    print(f'Задача {task_name} запущена.')
    task_processing_message = await asyncio.sleep(1, result=f'Задача {task_name} была выполнена.')
    print(task_processing_message)


async def main():
    task = asyncio.create_task(my_coroutine(), name='my_task')
    print(f"Задача {task.get_name()} создана, но еще не запущена")
    await task
    print('Ожидание выполнения my_task окончено, управление было возвращено в main().\nmain() завершает свою работу.')


asyncio.run(main())