## Proocess run in parallel
## CPU-Bound task: Task that heavy on CPU usage (e.g mathematical computation, data processing).
## Parallel execution -Multiple cores of CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")


if __name__ == "__main__":


    # create 2 processes
    t1 = multiprocessing.Process(target=square_numbers)
    t2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()

    # start the process
    t1.start()
    t2.start()

    ### wait for process to complete
    t1.join()
    t2.join()

    finished_time=time.time()-t

    print(finished_time)