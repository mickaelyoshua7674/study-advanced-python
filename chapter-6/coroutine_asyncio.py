import asyncio

async def hello():
    print("Hello async!")

h = hello()
print(h)

loop = asyncio.get_event_loop()
loop.run_until_complete(h)


async def wait_and_print(t:int|float, msg:str):
    await asyncio.sleep(t)
    print("Message: ", msg)

loop.run_until_complete(wait_and_print(1, "Hello"))