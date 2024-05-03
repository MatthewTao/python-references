import time
import random


class ContextManager:
    def __init__(self):
        print("init method called")

        self.dummy_thingy = "Hello World"

    def __enter__(self):
        print("enter method called")

        # Return is optional, but required if you want the object to be available in the context
        # Also doesn't have to be the object itself, can be something else
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("exit method called")

    def extra_method_that_can_be_called(self):
        print(f"\tCode within manager - {self.dummy_thingy}")


class Timer:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

        self.run_time = 0

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.perf_counter()
        self.run_time = self.end_time - self.start_time


if __name__ == "__main__":
    with ContextManager() as manager:
        print("\t\tPrinted from within the statement block")
        manager.extra_method_that_can_be_called()

    with Timer() as timer:
        random_numbers = [random.uniform(0.1, 0.2) for _ in range(10)]
    print(f"Took {timer.run_time*1000:.4f}ms to generate {random_numbers}")

    with Timer() as timer:
        print("testing string")
    print(f"Took {timer.run_time*1000:.4f}ms to print a string")
