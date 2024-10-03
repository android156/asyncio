import asyncio

dishes = {
    'Куриный суп': 118,
    'Бефстроганов': 13,
    'Рататуй': 49,
    'Лазанья': 108,
    'Паэлья': 51,
    'Утка по-пекински': 41,
}


async def cook_dish(duration):
    """Асинхронная задача, которая просто ждет указанное время."""
    task_name = asyncio.current_task().get_name()
    print(f"Приготовление {task_name} начато.")
    await asyncio.sleep(duration/10)
    print(f"Приготовление {task_name} завершено. за {duration/10}")
    return f'{task_name}: результат'


async def main():
    tasks = [asyncio.create_task(cook_dish(duration), name=name) for name, duration in dishes.items()]
    done, pending = await asyncio.wait(tasks, timeout=10)

    # Обрабатываем блюда, которые не успели приготовиться
    if pending:
        # Отменяем задачи по таймауту
        for task in pending:
            print(f"{task.get_name()} не успел(а,о) приготовиться и будет отменено.")
            task.cancel()
    # Статистика
    print(f"\nПриготовлено блюд: {len(done)}. Не успели приготовиться: {len(pending)}.")


asyncio.run(main())
