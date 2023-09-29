from threading import Timer
from concurrent.futures import Future

def network_request_async(number:int|float) -> Future:
    future = Future()
    result = {"success":True, "number":number, "square": number**2}
    Timer(1., lambda: future.set_result(result)).start()
    return future

def fetch_square(number:int|float):
    fut = network_request_async(number)

    def on_done_future(future:Future):
        response = future.result()
        if response["success"]:
            print(f"Square of {response['number']} is {response['square']}")
        
    fut.add_done_callback(on_done_future)

fetch_square(2)
fetch_square(3)
fetch_square(4)
print("Requests Submited")
