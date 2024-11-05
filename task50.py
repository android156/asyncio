import random
import asyncio


async def scan_port(address, port):
    await asyncio.sleep(0.1)
    if random.random() > 0.5:
        return f'Порт {port} на адресе {address} открыт'


async def scan_range(address, start_port, end_port):
    print(f'Сканирование портов с {start_port} по {end_port} на адресе {address}')
    tasks = [asyncio.create_task(scan_port(address, port)) for port in range(start_port, end_port + 1)]
    results = await asyncio.gather(*tasks)
    true_results = [result for result in results if result is not None]
    if len(true_results) == 0:
        print(f'Открытых портов на адресе {address} не найдено')
    else:
        for result in true_results:
            print(result)



async def main():
    address = "192.168.0.1"
    start_port = 80
    end_port = 85
    task = asyncio.create_task(scan_range(address, start_port, end_port))
    await task

asyncio.run(main())
