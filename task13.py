import asyncio

# Максимальное время для каста заклинания
max_cast_time = 5  # Секунды

# Ученики мага
students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]

spells = {'Огненный шар': 3, 'Ледяная стрела': 2, 'Щит молний': 4, 'Вихрь ветра': 4, 'Лечебное зелье': 1,
          'Призыв зверя': 6, 'Невидимость': 4, 'Защитный барьер': 3, 'Телепортация': 7, 'Призыв дождя': 2}


async def cast_spell(student, spell, cast_time):
    await asyncio.sleep(cast_time)
    return f"{student} успешно кастует {spell} за {cast_time} сек."


async def main():  # Максимальное время для завершения круга


    for spell, cast_time in spells.items():

        tasks = [asyncio.wait_for(cast_spell(student, spell, cast_time), timeout=max_cast_time) for student in students]
        try:
            results = await asyncio.gather(*tasks)
        except asyncio.TimeoutError:
            results = [f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. {student} успешно завершает заклинание с помощью shield." for student in students]

        for result in results:
            print(result)


asyncio.run(main())
