from concurrent.futures import ProcessPoolExecutor

def square(x):
    return x*x
if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        fut = executor.submit(square,[2])
        print(fut)

        result = executor.map(square,[2])
        print(result, list(result))