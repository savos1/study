import asyncio


# test

async def make_coffee():
    print("Начинаю готовить кофе...")
    await asyncio.sleep(3)  # Ждём 3 секунды (имитация приготовления)
    print("Кофе готов!")

async def make_toast():
    print("Начинаю делать тост...")
    await asyncio.sleep(2) 
    print("Тост готов!")

async def main():
    # Запускаем обе задачи "параллельно"
    await asyncio.gather(make_coffee(), make_toast())

asyncio.run(main())

# Декоратор для счёта вызовов функции

counter = 0

def count(func):
    global counter 
    counter += 1
    print(counter)
    return func

global_counter = 0

def count(func):
    def wrapper(*args, **kwargs):
        global global_counter
        global_counter += 1
        print(f"Всего вызовов функций: {global_counter}")
        return func(*args, **kwargs)
    return wrapper

@count
def test():
    print(764)

test()
test()
test()
test()
test()