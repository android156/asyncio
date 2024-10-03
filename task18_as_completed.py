import asyncio
import random

files = {
    "Начало": 4.2,
    "Матрица": 3.8,
    "Аватар": 5.1,
    "Интерстеллар": 2.6,
    "Паразиты": 6.0,
    "Джокер": 4.5,
    "Довод": 3.3,
    "Побег из Шоушенка": 5.4,
    "Криминальное чтиво": 2.9,
    "Форрест Гамп": 5.8
}

async def upload_file(filename, delay):
    await asyncio.sleep(delay)
    return f"{filename}: фильм загружен на сервер"


async def main():
    tasks = [asyncio.create_task(upload_file(filename, delay)) for filename, delay in files.items()]

    for completed_task in asyncio.as_completed(tasks):
        # completed_task - объект корутины, создаваемый функцией as_completed(), возвращающий результат завершенной задачи.
        result = await completed_task
        print(result)


asyncio.run(main())