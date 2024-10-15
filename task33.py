# Sample Output:
#
# Загрузка отчета Анализ доходности активов для пользователя Дмитрий Орлов остановлена. Введите
# новые данные
# Отчет: Обзор операционных расходов для пользователя Елена Кузнецова готов
# Отчет: Оценка инвестиционных рисков для пользователя Иван Смирнов готов
# Отчет: Прогнозирование движения денежных средств для пользователя Мария Петрова готов
# Отчет: Отчет о прибылях и убытках для пользователя Алексей Иванов готов

import asyncio

reports = [
    {"name": "Алексей Иванов", "report": "Отчет о прибылях и убытках", "load_time": 5},
    {"name": "Мария Петрова", "report": "Прогнозирование движения денежных средств", "load_time": 4},
    {"name": "Иван Смирнов", "report": "Оценка инвестиционных рисков", "load_time": 3},
    {"name": "Елена Кузнецова", "report": "Обзор операционных расходов", "load_time": 2},
    {"name": "Дмитрий Орлов", "report": "Анализ доходности активов", "load_time": 10}
]


async def download_data(report):
    if report["name"] == "Дмитрий Орлов":
        c_task = asyncio.current_task()
        await cancel_task(c_task)
    try:
        await asyncio.sleep(report["load_time"])
    except asyncio.CancelledError:
        print(f"Загрузка отчета {report["report"]} для пользователя {report["name"]} остановлена. Введите новые данные")

    print(f'Отчет: {report["report"]} для пользователя {report["name"]} готов')


async def cancel_task(task):
    task.cancel()


async def main():
    tasks = [asyncio.create_task(download_data(report)) for report in reports]
    await asyncio.gather(*tasks)


asyncio.run(main())
import asyncio

reports = [
    {"name": "Алексей Иванов", "report": "Отчет о прибылях и убытках", "load_time": 5},
    {"name": "Мария Петрова", "report": "Прогнозирование движения денежных средств", "load_time": 4},
    {"name": "Иван Смирнов", "report": "Оценка инвестиционных рисков", "load_time": 3},
    {"name": "Елена Кузнецова", "report": "Обзор операционных расходов", "load_time": 2},
    {"name": "Дмитрий Орлов", "report": "Анализ доходности активов", "load_time": 10}
]


async def download_data(report):
    if report["name"] == "Дмитрий Орлов":
        c_task = asyncio.current_task()
        await cancel_task(c_task)
    try:
        await asyncio.sleep(report["load_time"])
        print(f'Отчет: {report["report"]} для пользователя {report["name"]} готов')
    except asyncio.CancelledError:
        print(f"Загрузка отчета {report["report"]} для пользователя {report["name"]} остановлена. Введите новые данные")


async def cancel_task(task):
    task.cancel()


async def main():
    tasks = [asyncio.create_task(download_data(report)) for report in reports]
    await asyncio.gather(*tasks)


asyncio.run(main())
