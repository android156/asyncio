# put your python code here
import asyncio


async def activate_portal(activation_time):
    print(f'Активация портала в процессе, требуется времени: {activation_time} единиц')
    await asyncio.sleep(activation_time)
    activation_energy = activation_time * 2
    return activation_energy


async def perform_teleportation(activation, time):
    await activation
    print(f'Телепортация в процессе, требуется времени: {time} единиц')
    await asyncio.sleep(time)
    teleportation_result = time + 2
    return teleportation_result


async def recharge_portal(activation, time):
    await activation
    print(f'Подзарядка портала, требуется времени: {time} единиц')
    await asyncio.sleep(time)
    recharge_energy = time * 3
    return recharge_energy


async def check_portal_stability(activation, time):
    await activation
    print(f'Проверка стабильности портала, требуется времени: {time} единиц')
    await asyncio.sleep(time)
    portal_stability = time + 4
    return portal_stability


async def restore_portal(activation, time):
    await activation
    print(f'Восстановление портала, требуется времени: {time} единиц')
    await asyncio.sleep(time)
    restore_energy = time * 5
    return restore_energy


async def close_portal(tasks, close_time):
    for task in tasks[:-1]:
        await task
    print(f'Закрытие портала, требуется времени: {close_time} единиц')
    await asyncio.sleep(close_time)
    close_result = close_time - 1
    return close_result


async def portal_operator():
    operations = [activate_portal,
                  perform_teleportation,
                  recharge_portal,
                  check_portal_stability,
                  restore_portal,
                  close_portal,
                  ]
    tasks = []
    previous_task = None
    for i, operation in enumerate(operations, start=2):

        if i == 2:
            task = asyncio.create_task(operation(i))
            activation = task
        if i in [3, 4, 5, 6]:
            task = asyncio.create_task(operation(activation, i))
        if i == 7:
            task = asyncio.create_task(operation(tasks, i))

        tasks.append(task)

    results = await asyncio.gather(*tasks)

    print(f'Результат активации портала: {results[0]} единиц энергии')
    print(f'Результат телепортации: {results[1]} единиц времени')
    print(f'Результат подзарядки портала: {results[2]} единиц энергии')
    print(f'Результат проверки стабильности: {results[3]} единиц времени')
    print(f'Результат восстановления портала: {results[4]} единиц энергии')
    print(f'Результат закрытия портала: {results[5]} единиц времени')


asyncio.run(portal_operator())
