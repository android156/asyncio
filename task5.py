import asyncio
import time


async def coroutine_1(delay=0.1, start_time=None):
    print("Первое сообщение от корутины 1", time.time() - start_time)
    await asyncio.sleep(0.15)  # Первая задержка
    print("Второе сообщение от корутины 1", time.time() - start_time)
    await asyncio.sleep(0.25)  # Третья задержка
    print("Третье сообщение от корутины 1", time.time() - start_time)
    await asyncio.sleep(0.15)  # Вторая задержка
    print("Четвертое сообщение от корутины 1", time.time() - start_time)


async def coroutine_2(delay=0.1, start_time=None):
    print("Первое сообщение от корутины 2", time.time() - start_time)
    await asyncio.sleep(0.1)  # Третья задержка
    print("Второе сообщение от корутины 2", time.time() - start_time)
    await asyncio.sleep(delay)  # Вторая задержка
    print("Третье сообщение от корутины 2", time.time() - start_time)
    await asyncio.sleep(0.65)  # Первая задержка
    print("Четвертое сообщение от корутины 2", time.time() - start_time)


async def coroutine_3(delay=0.1, start_time=None):
    print("Первое сообщение от корутины 3", time.time() - start_time)
    await asyncio.sleep(delay)  # Третья задержка
    print("Второе сообщение от корутины 3", time.time() - start_time)
    await asyncio.sleep(0.3)  # Вторая задержка
    print("Третье сообщение от корутины 3", time.time() - start_time)
    await asyncio.sleep(0.5)  # Первая задержка
    print("Четвертое сообщение от корутины 3", time.time() - start_time)


async def main(start_time):
    await asyncio.gather(
        coroutine_1(0.2, start_time),
        coroutine_2(0.1, start_time),
        coroutine_3(0, start_time),
    )

start_time = time.time()
asyncio.run(main(start_time))