from random import random as rd
import asyncio

patient_info = [
    "Алексей Иванов: Прием для общего осмотра",
    "Мария Петрова: Чистка зубов",
    "Ирина Сидорова: Анализ крови",
    "Владимир Кузнецов: Рентгеновское исследование",
    "Елена Васильева: Вакцинация",
    "Дмитрий Николаев: Выписка рецепта",
    "Светлана Михайлова: Осмотр офтальмолога",
    "Никита Алексеев: Сеанс физиотерапии",
    "Ольга Сергеева: Срочный прием",
    "Анна Жукова: Регулярный контрольный осмотр"
]

async def producer(queue):
    print('Регистратура приступила к работе')
    for patient in patient_info:
        await queue.put(patient)
        await asyncio.sleep(rd())
        print(f'Регистратор добавил в очередь: {patient}')

    await queue.put(None)
    print('Регистратура закончила работу')


async def consumer(queue):
    print('Врач начал прием')
    while True:
        patient = await queue.get()
        if patient is None:
            break
        await asyncio.sleep(rd() * 5)
        print(f'Врач принял пациента: {patient}')
    print('Врач ушел домой')


async def main():
    queue = asyncio.Queue(maxsize=4)
    await asyncio.gather(producer(queue), consumer(queue))



asyncio.run(main())