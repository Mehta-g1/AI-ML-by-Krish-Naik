## MultiThread with ThreadPoolExecutor


from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
    time.sleep(1)
    return f"Number: {number}"

number = [1,2,3,4,5,6,7,8,9,0,1,2,3]


t = time.time()
with ThreadPoolExecutor(max_workers=3) as exe:
    results = exe.map(print_numbers, number)

for result in results:
    print(result)

finished_time = time.time()-t
print(finished_time)