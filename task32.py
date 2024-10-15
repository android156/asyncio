import asyncio


async def get_task_id():
    await asyncio.sleep(1)
    task_id = id(asyncio.current_task())
    return task_id


async def main():
    tasks = [asyncio.create_task(get_task_id()) for _ in range(10)]
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())

