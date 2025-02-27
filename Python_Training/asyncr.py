import asyncio

# async def main():
#     print('Hello ...')
#     await asyncio.sleep(1)
#     print('... World!')

# asyncio.run(main())

async def say_hello():
    print("Hello....")
    await asyncio.sleep(3)
    print("Hello after 3 seconds.")

async def say_goodbye():
    print("GoodBye....")
    await asyncio.sleep(4)
    print("GoodBye after 4 seconds.")

async def main():
    await asyncio.gather(say_hello(), say_goodbye())

asyncio.run(main())