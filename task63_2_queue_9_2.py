import asyncio

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


async def producer(queues: dict[str, asyncio.Queue], patient_info):
    for patient in patient_info:
        await asyncio.sleep(0.5)
        await queues[patient['direction']].put(patient)
        print(f"Регистратор добавил в очередь: {patient['name']}, "
              f"направление: {patient['direction']}, "
              f"процедура: {patient['procedure']}")


async def consumer(queue: asyncio.Queue, doctor_type):
    while True:
        patient = await queue.get()
        await asyncio.sleep(0.5)
        print(f"{doctor_type} принял пациента: {patient['name']}, процедура: {patient['procedure']}")
        queue.task_done()


async def main():
    # Полный список вшит в задачу, вставлять его в поле ответа нет необходимости
    # patient_info = []

    directions: set = set(p['direction'] for p in patient_info)
    queues: dict[str, asyncio.Queue] = {k: asyncio.Queue() for k in directions}

    task_prod = asyncio.create_task(producer(queues, patient_info))
    tasks_cons: dict[str, asyncio.Task] = {direct: asyncio.create_task(consumer(queues[direct], direct))
                                           for direct in directions}

    await task_prod

    for direct in directions:
        await queues[direct].join()
        tasks_cons[direct].cancel()


asyncio.run(main())
