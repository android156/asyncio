import asyncio
# Объявите функцию publish_post: принимает на вход текст поста и имитирует публикацию нового поста на блоге Васи


# Объявите функцию notify_subscribers: принимает на вход список подписчиков и имитирует отправку уведомления каждому подписчику
async def publish_post(text):
    await asyncio.sleep(1)
    return f"Пост опубликован: {text}"


async def notify_subscribers(subscriber):
    await asyncio.sleep(1)
    return f'Уведомление отправлено {subscriber}'


async def main():
    post_text = "Hello world!"
    subscribers = ["Alice", "Bob", "Charlie", "Dave", "Emma", "Frank", "Grace", "Henry", "Isabella", "Jack"]
    tasks = [asyncio.create_task(notify_subscribers(subscriber)) for subscriber in subscribers]
    tasks.insert(0, asyncio.create_task(publish_post(post_text)))
    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

# запускаем асинхронную функцию main()
if __name__ == '__main__':
    asyncio.run(main())