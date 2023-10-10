import threading, time

def thread_count_down(name:str, delay:int|float):
    counter = 5
    while counter:
        time.sleep(delay)
        print(f"Thread {name} counting down: {counter}...")
        counter -= 1

class MyThread(threading.Thread):
    def __init__(self, name:str, delay:int|float) -> None:
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
    
    def run(self) -> None:
        print(f"Starting thread {self.name}")
        thread_count_down(self.name, self.delay)
        print(f"Finished thread {self.name}")