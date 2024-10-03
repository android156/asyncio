import asyncio


async def count1(name):
    for i in range(3, 0, -1):
        print(f"{name} Обратный отсчет: {i}")
        await asyncio.sleep(0)


async def count2(name):
    for i in range(3, 0, -1):
        print(f"{name} Обратный отсчет: {i}")


async def main():
    await asyncio.gather(count1('count1_1'), count1('count1_2'), count2('count2_1'))


asyncio.run(main())



