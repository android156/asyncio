import asyncio
import random

server_names = {
        "1": "Server_Alpha", "2": "Server_Beta", "3": "Server_Gamma",
        "4": "Server_Delta", "5": "Server_Epsilon"}

async def load_data(server_name):
    print(f'Загрузка данных с сервера {server_name} началась')
    await asyncio.sleep(random.randint(0, 5))
    print(f'Загрузка данных с сервера {server_name} завершена')

async def main():
    async with asyncio.TaskGroup() as tg:
        [tg.create_task(load_data(server_name)) for server_name in server_names.values()]


asyncio.run(main())