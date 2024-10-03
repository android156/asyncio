import asyncio

def check_loop_status(loop):
    if loop:
        print(f"Цикл событий активен: {loop.is_running()}, Цикл событий закрыт: {loop.is_closed()}.")
    else:
        print(f"Цикл событий активен: False, Цикл событий закрыт: False.")

async def main():
    loop = asyncio.get_event_loop()
    check_loop_status(loop)
    print("Корутина завершена")

loop = asyncio.new_event_loop()
loop.run_until_complete(main())
loop.close()