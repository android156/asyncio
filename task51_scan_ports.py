import random
import asyncio


async def scan_port(address, port):
    """
        Асинхронная функция, имитирующая сканирование порта на заданном ip-адресе.
    """
    await asyncio.sleep(1)
    if random.randint(0, 100) == 1:
        # Печать сообщения об обнаружении открытого порта.
        print(f'Port {port} on {address} is open')
        return port


async def scan_range(address, start_port, end_port):
    """
        Асинхронная функция, проверяющая состояние диапазона портов по указанному адресу.
    """
    # Печать сообщения о начале сканирования диапазона портов для заданного ip-адреса.
    print(f"Scanning ports {start_port}-{end_port} on {address}")
    tasks = [asyncio.create_task(scan_port(address, port)) for port in range(start_port, end_port + 1)]
    results = await asyncio.gather(*tasks)
    true_results = [result for result in results if result is not None]
    return address, true_results


async def main(dct):
    """
        Основная асинхронная функция, управляющая процессом сканирования портов из переданного в нее словаря.
    """
    tasks = [asyncio.create_task(scan_range(address, port_range[0], port_range[1])) for address, port_range in
             dct.items()]
    results = await asyncio.gather(*tasks)
    for result in results:
        address, open_ports = result
        if len(open_ports) > 0:
            print(f'Всего найдено открытых портов {len(open_ports)} {open_ports} для ip: {address}')


ip_dct = {'192.168.0.1': [0, 100], '192.168.0.2': [225, 300], '192.168.2.5': [150, 185]}
# Запуск асинхронного приложения с передачей в main() словаря ip_dct
asyncio.run(main(ip_dct))
