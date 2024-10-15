import asyncio

# Словарь файлов и их размеров
files = {
    "file1.mp4": 32,
    "image2.png": 24,
    "audio3.mp3": 16,
    "document4.pdf": 8,
    "archive5.zip": 40,
    "video6.mkv": 48,
    "presentation7.pptx": 12,
    "ebook8.pdf": 20,
    "music9.mp3": 5,
    "photo10.jpg": 7,
    "script11.py": 3,
    "database12.db": 36,
    "archive13.rar": 15,
    "document14.docx": 10,
    "spreadsheet15.xls": 25,
    "image16.gif": 2,
    "audioBook17.mp3": 60,
    "tutorial18.mp4": 45,
    "code19.zip": 22,
    "profile20.jpg": 9
}

async def download_file(file_name, size, n_speed):
    dl_time = round(size/n_speed, 1)
    print(f'Начинается загрузка файла: {file_name}, его размер {size} мб, время загрузки составит {dl_time} сек')
    await asyncio.sleep(dl_time)
    print(f'Загрузка завершена: {file_name}')

async def monitor_tasks(tasks):
    for task in tasks:
        if task.done():
            print(f'Задача {task.get_name()}: завершена, Статус задачи {task.done()}')
        else:
            print(f'Задача {task.get_name()}: в процессе, Статус задачи {task.done()}')


async def main():
    nw_speed = 8
    pending = [True]
    done = [False]
    tasks = [asyncio.create_task(download_file(file_name, size, nw_speed), name=file_name) for file_name, size in files.items()]

    while pending:
        await monitor_tasks(tasks)
        done, pending = await asyncio.wait(tasks, timeout=1)

    await monitor_tasks(done)
    print('Все файлы успешно загружены')


asyncio.run(main())