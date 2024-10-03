import asyncio

# Максимальное время для каста заклинания
max_cast_time = 5  # Секунды

# Ученики мага
students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]

spells = {'Огненный шар': 3, 'Ледяная стрела': 2, 'Щит молний': 4, 'Вихрь ветра': 4, 'Лечебное зелье': 1,
          'Призыв зверя': 6, 'Невидимость': 4, 'Защитный барьер': 3, 'Телепортация': 7, 'Призыв дождя': 2}


async def cast_spell(student, spell, cast_time):
    try:
        await asyncio.wait_for(asyncio.sleep(cast_time), timeout=max_cast_time)
        return f"{student} успешно кастует {spell} за {cast_time} сек."
    except asyncio.TimeoutError:
        return f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. {student} успешно завершает заклинание с помощью shield."


async def main():  # Максимальное время для завершения круга
        tasks = [asyncio.shield(cast_spell(student, spell, cast_time)) for spell, cast_time in spells.items() for student in students]
        results = await asyncio.gather(*tasks)
       
        for result in results:
            print(result)


asyncio.run(main())
