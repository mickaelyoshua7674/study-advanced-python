from time import time

class Timer:
    def __init__(self, timeout:int|float) -> None:
        self.timeout = timeout
        self.start = time()
    
    def done(self) -> bool:
        return time()-self.start > self.timeout

    def on_timer_done(self, callback:callable) -> None:
        self.callback = callback

timer = Timer(1.)
timer.on_timer_done(lambda: print("Timer is done!"))
while True:
    if timer.done():
        timer.callback()
        break
