import asyncio

async def my_coroutine(num):
    await asyncio.sleep(num)
    return num

async def generate_completed_tasks(tasks):
    for task in asyncio.as_completed(tasks):
        result = await task
        yield result

async def main():
    tasks = [my_coroutine(1), my_coroutine(2), my_coroutine(0.5)]
    async for result in generate_completed_tasks(tasks):
        print(result)

# Запускаем главную асинхронную функцию
asyncio.run(main())