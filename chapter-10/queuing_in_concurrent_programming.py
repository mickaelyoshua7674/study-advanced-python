import queue, threading, time

my_queue = queue.Queue()

def print_factors(x:int) -> None:
    result_string = f"Positive factors of {x} are: "
    for i in range(1, x+1):
        if x%i == 0:
            result_string += str(i) + " "
    result_string += "\n" + "_"*20
    print(result_string)

def process_queue():
    while True:
        try:
            x = my_queue.get(block=False)
        except queue.Empty:
            return
        else:
            print_factors(x)
        time.sleep(1)

class MyThread(threading.Thread):
    def __init__(self, name:str) -> None:
        threading.Thread.__init__(self)
        self.name = name
    
    def run(self):
        print(f"Starting thread {self.name}...")
        process_queue()
        print(f"Exiting thread {self.name}...")

input = [1,10,4,3]

for x in input:
    my_queue.put(x)

threads = [MyThread(name) for name in ("A","B","C")]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# thread1 = MyThread("A")
# thread2 = MyThread("B")
# thread3 = MyThread("C")

# thread1.start()
# thread2.start()
# thread3.start()

# thread1.join()
# thread2.join()
# thread3.join()

print("Done")