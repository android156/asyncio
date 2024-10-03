import asyncio

runners = {
    "Молния Марк": 12.8,
    "Ветреный Виктор": 13.5,
    "Скоростной Степан": 11.2,
    "Быстрая Белла": 10.8,

}


async def run_lap(name, speed):
    time = round(100 / speed, 2)
    await asyncio.sleep(time)
    print(f"{name} завершил круг за {time} секунд")


async def main(max_time=10):  # Максимальное время для завершения круга 10 сек
    results = await asyncio.gather(
        *[asyncio.wait_for(run_lap(name, speed), timeout=10) for name, speed in runners.items()],
        return_exceptions=True)


async def run_lap2(name, speed):
    distance = 100  # Длина круга в метрах
    time_needed = round(distance / speed, 2)  # Время, необходимое для завершения круга
    await asyncio.sleep(time_needed)  # Имитация бега
    print(f"{name} завершил круг за {time_needed} секунд")


async def main2(max_time=10):  # Максимальное время для завершения круга
    tasks = [run_lap(name, speed) for name, speed in runners.items()]
    try:
        await asyncio.wait_for(asyncio.gather(*tasks), max_time)
    except asyncio.TimeoutError:
        pass


asyncio.run(main())
asyncio.run(main2())
