# put your python code here
import asyncio
import random

random.seed(5)

def on_data_parsed(task):
    result = task.result()
    if len(result) > 0:
        print(f"Найдено {len(result)} файлов для скачивания: {result}")


async def parse_data(url):
    await asyncio.sleep(1)
    if random.choice([True, False]):
        file_urls = [f"{url}/example_file.zip"]
    else:
        file_urls = []
    return file_urls


async def main():
    urls = [
        "https://example.com/data1",
        "https://example.com/data2",
        "https://example.com/data3"
    ]
    for url in urls:
        task = asyncio.create_task(parse_data(url))
        task.add_done_callback(on_data_parsed)  # Регистрация callback-функции
        await task

asyncio.run(main())
