import asyncio
import itertools
import random

users = ['user1', 'user2', 'user3']
products = ['iPhone 14', 'Samsung Galaxy S23', 'MacBook Pro', 'Dell XPS 13', 'Sony WH-1000XM5', 'Apple Watch Series 8',
            'Kindle Paperwhite', 'GoPro Hero 11', 'Nintendo Switch', 'Oculus Quest 2']
actions = ['просмотр', 'покупка', 'добавление в избранное']


async def user_action_generator():
    for user, product, action in itertools.product(users, products, actions):
        yield {'user_id': random.choice(users),
               'action': random.choice(actions),
               'product_id': random.choice(products)}


async def main():
    async for situation in user_action_generator():
        print(situation)
        if situation['user_id'] == 'user1':
            break


asyncio.run(main())