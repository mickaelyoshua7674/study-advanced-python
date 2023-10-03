from threading import Timer

def on_done(result:dict):
    print(result)

def network_request_async(number:int|float, on_done:callable):
    def timer_done():
        on_done({"success":True, "number":number, "square": number**2})
    
    print(f"Requests will take 1s")
    Timer(1, timer_done).start()

def fetch_square(number:int|float):
    def on_done(response:dict):
        if response["success"]:
            print(f"Square of {response['number']} is {response['square']}\n")
    
    network_request_async(number, on_done)


fetch_square(2)
fetch_square(3)
fetch_square(4)
print("Requests Submited")
