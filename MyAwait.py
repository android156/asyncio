import asyncio

# Асинхронная функция, имитирующая чтение данных из файла
async def read_data_from_file(filename):
    print(f"Начинаем чтение из файла {filename}")
    await asyncio.sleep(2)  # # Имитация задержки для чтения файла
    print(f"Чтение из файла {filename} завершено")
    return f"данные из {filename}"

# Асинхронная функция, имитирующая отправку данных в интернет
async def send_data_to_internet(data):
    print("Начинаем отправку данных в интернет")
    await asyncio.sleep(3)  # Имитация задержки для отправки данных
    print("Отправка данных в интернет завершена")

# Главная асинхронная функция, которая управляет выполнением программы
async def main():
    filename = "example.txt"
    # Чтение данных из файла
    file_data = await read_data_from_file(filename)
    # Отправка прочитанных данных в интернет
    await send_data_to_internet(file_data)

asyncio.run(main())