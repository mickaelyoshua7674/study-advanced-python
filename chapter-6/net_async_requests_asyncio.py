import asyncio

async def network_request(number:int):
    await asyncio.sleep(1.)
    return {"success":True, "number":number, "square": number**2}

async def fetch_square(number:int):
    response = await network_request(number)
    if response["success"]:
        print(f"Square of {response['number']} is {response['square']}")

loop = asyncio.get_event_loop()

# # Run synchronously
# loop.run_until_complete(fetch_square(2))
# loop.run_until_complete(fetch_square(3))
# loop.run_until_complete(fetch_square(4))

# Run asynchronously
asyncio.ensure_future(fetch_square(2))
asyncio.ensure_future(fetch_square(3))
asyncio.ensure_future(fetch_square(4))

loop.run_forever()

