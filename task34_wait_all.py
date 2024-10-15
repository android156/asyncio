import asyncio

warehouse_store = {
    "Диван": 15,
    "Обеденный стол": 10,
}

order = {'Диван': 5, 'Обеденный_стол': 3, 'Табуретка': 50, 'Гардероб': 1}


# Тут пишите ваш код:
async def check_store(item, quantity):
    task = asyncio.current_task()
    print(warehouse_store.get(item, 0))
    if not warehouse_store.get(item, 0):
        task.set_name(f"Отсутствует: {item}")
    elif warehouse_store.get(item, 0) < quantity:
        task.set_name(f"Частично в наличии: {item}")
    else:
        task.set_name(f"В наличии: {item}")


async def main():
    tasks = [asyncio.create_task(check_store(item, quantity)) for item, quantity in order.items()]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)

    sort_result = [task.get_name() for task in done]
    sort_result.sort()
    for task_name in sort_result:
        print(task_name)

asyncio.run(main())


# async def check_store(item, quantity):
#     exist = warehouse_store.get(item, 0)
#     status = ['Отсутствует', 'Частично в наличии', 'В наличии'][bool(exist) + (exist >= quantity)]
#     asyncio.current_task().set_name(f'{status}: {item}')
#
#
# async def main():
#     tasks = [asyncio.create_task(check_store(item, quantity)) for item, quantity in order.items()]
#     result = await asyncio.gather(*tasks)
#     print(*sorted(task.get_name() for task in tasks), sep='\n')
#
#
# asyncio.run(main())