import asyncio
import random
import itertools

shapes = ["circle", "star", "square", "diamond", "heart"]
colors = ["red", "blue", "green", "yellow", "purple"]
actions = ["change_color", "explode", "disappear"]

async def launch_firework(shape, color, action):
    print(f"Запущен {color} {shape} салют, в форме {action}!!!")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Салют {color} {shape} завершил выступление {action}")

async def main():
    async with asyncio.TaskGroup() as tg:
        [tg.create_task(launch_firework(shape, color, action)) for shape, color, action in itertools.product(shapes, colors, actions)]

asyncio.run(main())