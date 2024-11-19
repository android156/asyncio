import asyncio
from asyncio import LifoQueue


async def autosave(queue):
    for i in range(1, 21):
        await asyncio.sleep(.1)
        await queue.put(i)
        print(f"Автосохранение игры через {i} часов")


async def simulate_gameplay(queue):
    while True:
        a_s = await queue.get()
        if a_s % 5 == 0:
            print(f"Загружена последняя версия игры: {a_s}")
        if a_s == 20:
            break


async def main():
    queue = LifoQueue()
    await asyncio.gather(autosave(queue), simulate_gameplay(queue))
    print('Игра пройдена!')


# async def autosave(stack):
#
#     for i in range(1, 21):
#         print(f"Автосохранение игры через {i} часов")
#         if i % 5 == 0:
#             i = await stack.put(i)
#         await asyncio.sleep(0.1)
#
# async def simulate_gameplay(stack):
#
#     while True:
#         i = await stack.get()
#         print(f"Загружена последняя версия игры: Автосохранение {i}")
#         stack.task_done()
#
# async def main():
#
#     stack = LifoQueue()
#     asyncio.create_task(simulate_gameplay(stack))
#     await autosave(stack)
#     await stack.join()
#     print("Игра пройдена!")


asyncio.run(main())


