import asyncio
import random

# Не менять!
random.seed(1)


async def collect_gold():
    await asyncio.sleep(random.randint(1, 5))
    return random.randint(10, 50)


async def main():
    tasks = [asyncio.create_task(collect_gold()) for _ in range(10)]
    all_gold = 0
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        all_gold += result
        print(f'Собрано {result} единиц золота.')
        print(f"Общее количество золота: {all_gold} единиц.")
        print()


asyncio.run(main())
