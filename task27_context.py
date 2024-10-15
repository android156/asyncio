import asyncio
import contextvars

order_state = contextvars.ContextVar('order_state')
states = ["Принят", "Обрабатывается", "Отправлен"]

def set_order_state(state):
    order_state.set(state)


async def process_order(order_id):
    for state in states:
        await asyncio.sleep(1, set_order_state(state))
        print(f"Заказ {order_id} сейчас в состоянии: {order_state.get('Unknown')}")

async def main():
    orders = ["Заказ1", "Заказ123", "Заказ12345"]
    tasks = [asyncio.create_task(process_order(order_id)) for order_id in orders]
    await asyncio.gather(*tasks)


asyncio.run(main())