import asyncio


# Корутина для задачи, имитирующей выполнение критической задачи.
async def my_coroutine():
    print("Агент приступил к выполнению своего задания.")
    await asyncio.sleep(1)
    # Если задача не была отменена выведем это сообщение
    print("Злодей побежден! Миссия успешно завершена!")


# Корутина для попытки отмены выполнения защищенной задачи.
async def cancel_coroutine(future):
    await asyncio.sleep(0.5)
    future.cancel()
    print("Банг!!! Злодей стреляет в агента!")
    # Можно посмотреть состояние shield_obj после отмены.
    print(f'shield_obj отменен: {future.cancelled()}')
    print(f'shield_obj завершен: {future.done()}')


async def main():
    # Создаем защитный объект shield_obj.
    shield_obj = asyncio.shield(my_coroutine())
    # Можно посмотреть тип shield_obj
    print(f'Тип защитного объекта shield: {type(shield_obj).__name__}') # Future
    print("Бронежилет надет на агента.")
    cancel_task = asyncio.create_task(cancel_coroutine(shield_obj))
    print("Пистолет злодея заряжен.")
    # В случае получения shield_obj asyncio.CancelledError выводим сообщение.
    try:
        await asyncio.gather(shield_obj, cancel_task)
    except asyncio.CancelledError:
        print("Внимание! Бронежилет разрушен!")
    await asyncio.sleep(1)


asyncio.run(main())