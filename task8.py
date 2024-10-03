import asyncio

places = [
    "начинает путешествие",
    "находит загадочный лес",
    "переправляется через реку",
    "встречает дружелюбного дракона",
    "находит сокровище"]

roles = ["Искатель приключений", "Храбрый рыцарь", "Отважный пират"]


async def counter(name, delay=.1):
    for place in places:
        print(f'{name} {place}...')
        await asyncio.sleep(delay)


async def main():
    tasks = [asyncio.create_task(counter(name)) for name in roles]
    # Дождитесь выполнения всех созданных задач в главной корутине с помощью await.
    await asyncio.gather(*tasks)


asyncio.run(main())