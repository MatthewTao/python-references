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


if __name__ == "__main__":
    number_of_iterations = int(input("How many iterations? [default=100] ") or 100)
    numbers = [5000000 + x for x in range(number_of_iterations)]

    start_time = time.perf_counter()
    find_sum_multi(numbers)
    end_time = time.perf_counter()

    print(f"Multiprocessing took {int(end_time - start_time)} seconds")

    start_time = time.perf_counter()
    find_sum(numbers)
    end_time = time.perf_counter()

    print(f"No multiprocessing took {int(end_time - start_time)} seconds")
