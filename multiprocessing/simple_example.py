import multiprocessing
import time


def cpu_bound(number):
    return sum(i * i for i in range(number))

def find_sum(numbers):
    for number in numbers:
        cpu_bound(number)

def find_sum_multi(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)

start_time = time.time()
numbers = [5000000 + x for x in range(50)]
find_sum(numbers)
end_time = time.time()

print(f'Took {int(end_time - start_time)} seconds')
