import asyncio


class AsyncTransaction:
    # Метод для выполнения асинхронной операции перед началом контекста
    async def __aenter__(self):
        print("Starting transaction")
        await asyncio.sleep(0.5)

    # Метод для выполнения асинхронной операции после завершения контекста
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Ending transaction")
        await asyncio.sleep(0.5)


async def perform_transaction():
    # Используем async with для корректного выполнения асинхронных операций перед началом и после завершения контекста
    async with AsyncTransaction():
        print("Performing transaction operations")
        await asyncio.sleep(1)


asyncio.run(perform_transaction())