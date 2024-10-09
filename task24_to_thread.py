import asyncio
import threading
import time


# Блокирующая функция
def blocking_fn(arg1, arg2):
    # Печать сообщения о старте и номере используемого потока.
    print(f"Старт blocking_fn() в потоке c id {threading.current_thread().ident} в {time.strftime('%X')}")

    # Обратите внимание, что time.sleep() может быть заменен любой блокирующей
    # IO-bound операцией, например операцией с файлами.
    time.sleep(arg1)  # Имитация выполнения длительной операции используем arg1.
    print(f"Завершение blocking_fn() в {time.strftime('%X')}")
    return f'В blocking_fn() были переданы два аргумента arg1: {arg1} и arg2: {arg2}'


# Функция асинхронного sleep()
async def sleep_fn():
    # Печать сообщения о старте и номере используемого потока.
    print(f"Старт sleep_fn() в потоке c id {threading.current_thread().ident} в {time.strftime('%X')}")
    await asyncio.sleep(1)
    print(f"Завершение sleep_fn() в {time.strftime('%X')}")


async def main():
    # Печать сообщения о старте и номере используемого потока
    print(f"Старт main в потоке c id {threading.current_thread().ident} в {time.strftime('%X')}")

    # Создание корутины, для запуска в независимом потоке, передача аргументов.
    coro = asyncio.to_thread(blocking_fn, 1, 'Привет')

    # Проверка типа объекта для coro
    print(f'Тип объекта coro: {type(coro)}')
    result = await asyncio.gather(coro, sleep_fn(), sleep_fn())
    print(result[0])
    print(f"Завершение main в {time.strftime('%X')}")


start = time.time()
asyncio.run(main())
print(f'Время выполнения программы: {(time.time() - start)}')