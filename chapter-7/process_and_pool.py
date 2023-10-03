import multiprocessing
from time import sleep

# class Process(multiprocessing.Process):
#     def __init__(self, id:int) -> None:
#         super(Process, self).__init__()
#         self.id = id

#     def run(self):
#         sleep(1)
#         print(f"I'm the process with id: {self.id}")

# if __name__ == "__main__":
#     p = Process(0)
#     p.start()
#     print("Fim")

# if __name__ == "__main__":
#     p = Process(0)
#     p.start()
#     p.join() # wait for process to finish
#     print("Fim")

# if __name__ == "__main__":
#     processes = Process(1), Process(2), Process(3), Process(4)
#     [p.start() for p in processes] # execution is concurrent and the order is unpredictable

def square(x):
    return x*x
inputs = [0,1,2,3,4]
if __name__ == "__main__":
    with multiprocessing.Pool() as pool: # multiprocessing.Pool(processes={number desired of cores / default is all availables})
        outputs_async = pool.map_async(square, inputs)
        print(f"Outputs map_async {outputs_async.get()}")
        outputs = pool.map(square, inputs)
        print(f"Outputs map {outputs}")