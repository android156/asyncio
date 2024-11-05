# put your python code here
import asyncio

codes = ["56FF4D", "A3D2F7", "B1C94A", "F56A1D", "D4E6F1",
         "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
         "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F2"]

messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
            "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
            "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!",
            "Всего наилучшего!"]

def is_code_odd(code):
    if code[-1] in ['1', '3', '5', '7', '9', 'B', 'D', 'F',]:
        return True

async def print_message(code):
    if is_code_odd(code):
        print(f'Сообщение: {messages[codes.index(code)]}')
    else:
        print(f'Сообщение: Неверный код, сообщение скрыто')
    return code


def print_code(task):  # Callback-функция
    print(f"Код: {task.result()}")


async def main():
    for code in codes:
        task = asyncio.create_task(print_message(code))
        task.add_done_callback(print_code)  # Регистрация callback-функции
        await task


asyncio.run(main())
