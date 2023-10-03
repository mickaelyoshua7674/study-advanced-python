from multiprocessing import Lock, Process, Value

def run(lock, counter:int):
    for _ in range(1000):
        with lock: # acquire the lock
            counter.value += 1
        # release the lock

if __name__ == "__main__":
    lock = Lock()
    counter = Value("i")
    counter.value = 0

    processes = [Process(target=run, args=(lock, counter)) for _ in range (4)]
    [p.start() for p in processes]
    [p.join() for p in processes] # processes are done
    print(counter.value)