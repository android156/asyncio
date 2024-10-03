import asyncio
import random

# Не менять.
random.seed(1)


class MailServer:
    def __init__(self):
        self.mailbox = ["Привет!", "Встреча в 15:00", "Важное уведомление", "Реклама"]

    async def check_for_new_mail(self):
        if random.random() < 0.1:
            return "Ошибка при проверке новых писем."
        return random.choice([True, False])

    async def fetch_new_mail(self):
        mail = random.choice(self.mailbox)
        return f"Новое письмо: {mail}"


# Тут пишите ваш код
async def check_mail(server):
    while True:
        response = await server.check_for_new_mail()
        if response == "Ошибка при проверке новых писем.":
            print(response)
            break
        else:
            if response:
                print(await server.fetch_new_mail())
            else:
                print("Новых писем нет.")
        await asyncio.sleep(1)


async def main():
    server = MailServer()
    task = asyncio.create_task(check_mail(server))
    await task


asyncio.run(main())