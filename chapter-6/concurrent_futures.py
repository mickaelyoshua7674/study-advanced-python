from concurrent.futures import Future

fut = Future()
print(fut)

fut.set_result("Hello")
print(fut)
print(fut.result())