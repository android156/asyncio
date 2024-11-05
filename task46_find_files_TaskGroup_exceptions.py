import asyncio
import random

files = ['image.png',
         'image2.png',
         'file.csv',
         'file1.txt',
         'image.png',
         'image3.png',
         'file2.csv',
         'file2.txt', ]


# Не менять функцию
async def download_file(file_name):
    await asyncio.sleep(0.2)
    errors = [FileNotFoundError(f'{file_name}: Файл не найден'),
              PermissionError(f'{file_name}: Нет прав на доступ к файлу'),
              TimeoutError(f'{file_name}: Превышено время ожидания для скачивания файла')]
    if random.random() > 0.5:
        raise random.choice(errors)
    else:
        await asyncio.sleep(0.1)
        return f'Файл {file_name} успешно скачан'


# Ваш код пишите тут:
async def main():
    result = []
    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(download_file(file), name=file) for file in files]

    except* Exception as e:
        for error in e.exceptions:
            print(error)

    for task in tasks:
        # if not task.exception() and not task.cancelled():
        #     result.append(task.result())
        print(f'{task.get_name()}: done={task.done()}, cancelled={task.cancelled()}, ')


    print('Готово!!!', result)

asyncio.run(main())
