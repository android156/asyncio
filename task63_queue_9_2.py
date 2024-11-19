import asyncio
from random import random as rd

patient_info = [
    {'name': 'Алексей Иванов', 'direction': 'Терапевт', 'procedure': 'Прием для общего осмотра'},
    {'name': 'Мария Петрова', 'direction': 'Хирург', 'procedure': 'Малая операция'},
    {'name': 'Ирина Сидорова', 'direction': 'ЛОР', 'procedure': 'Осмотр уха'},
    {'name': 'Владимир Кузнецов', 'direction': 'Терапевт', 'procedure': 'Консультация'},
    {'name': 'Елена Васильева', 'direction': 'Хирург', 'procedure': 'Хирургическая процедура'},
    {'name': 'Дмитрий Николаев', 'direction': 'ЛОР', 'procedure': 'Промывание носа'},
    {'name': 'Светлана Михайлова', 'direction': 'Терапевт', 'procedure': 'Рутинный осмотр'},
    {'name': 'Никита Алексеев', 'direction': 'Хирург', 'procedure': 'Операция на колене'},
    {'name': 'Ольга Сергеева', 'direction': 'ЛОР', 'procedure': 'Лечение ангины'},
    {'name': 'Анна Жукова', 'direction': 'Терапевт', 'procedure': 'Вакцинация'}
]


async def producer(queue):
    for patient in patient_info:
        await queue.put(patient)
        await asyncio.sleep(rd())
        print(
            f"Регистратор добавил в очередь: {patient['name']}, направление: {patient['direction']}, процедура: {patient['procedure']}")

    await queue.put(None)
    print('Регистратура закончила работу')


async def consumer(queue, locks):
    while True:
        patient = await queue.get()
        if patient is None:
            break
        if patient['direction'] == 'Терапевт':
            lock = locks[0]
        elif patient['direction'] == 'Хирург':
            lock = locks[1]
        else: lock = locks[2]

        async with lock:
            await asyncio.sleep(rd() * 5)
            print(f"{patient['direction']} принял пациента: {patient['name']}, процедура: {patient['procedure']}")


async def main():
    queue = asyncio.Queue()
    locks = [asyncio.Lock() for _ in range(3)]

    await asyncio.gather(producer(queue), consumer(queue, locks))
    # Полный список вшит в задачу, вставлять его в поле ответа нет необходимости
    # patient_info = []




asyncio.run(main())
