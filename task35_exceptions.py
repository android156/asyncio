import asyncio

files = ['image.png', 'image2.png', 'file.csv', 'file1.txt']
missed_files = ['file.csv', 'image2.png', ]

# Не менять функцию
async def download_file(file_name):
    await asyncio.sleep(1)
    if file_name in missed_files:
        raise FileNotFoundError(f'Файл {file_name} не найден')
    else:
        await asyncio.sleep(1)
        return f'Файл {file_name} успешно скачан'

# Ваш код пишите тут:
async def main():
    tasks = [asyncio.create_task(download_file(file)) for file in files]
    await asyncio.gather(*tasks, return_exceptions=True)

    for i, task in enumerate(tasks, start=1):
        # Получаем исключение из задачи, если оно возникло, и выводим информацию о нем
        exc = task.exception()
        if exc:
            print(exc)

# # Ваш код пишите тут:
# async def main():
#     tasks = [asyncio.create_task(download_file(file_name)) for file_name in files]
#     done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
#     for task in done:
#         if task.exception():
#             print(task.exception())


asyncio.run(main())
