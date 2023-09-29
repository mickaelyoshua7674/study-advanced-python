import threading, time

def wait_and_print(t:float, msg:str):
    time.sleep(t)
    print(msg)

def wait_and_print_async(t:float, msg:str):
    def callback():
        print(msg)

    threading.Timer(t, callback).start()


wait_and_print(1., "First Call")
wait_and_print(1., "Second Call")
wait_and_print_async(1., "First Call Async")
wait_and_print_async(1., "Second Call Async")