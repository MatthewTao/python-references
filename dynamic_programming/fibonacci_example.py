import time
from functools import cache


def brute_force():
    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)
    start_time = time.perf_counter_ns()
    fib(20)
    print(f"Brute force runtime: {(time.perf_counter_ns() - start_time) / 1000}ms")


def memoization():
    def fib_rec(n, memo: dict):
        # Base case
        if n <= 1:
            return n

        # To check if output already exists
        if memo.get(n):
            return memo[n]

        # Calculate and save output for future use
        memo[n] = fib_rec(n - 1, memo) + fib_rec(n - 2, memo)
        return memo[n]

    def fib(n):
        memo = {}
        return fib_rec(n, memo)

    start_time = time.perf_counter_ns()
    fib(20)
    print(f"Memo runtime: {(time.perf_counter_ns() - start_time) / 1000}ms")


def built_in_memoization():
    """
    Interesting that the built-in memoization is slower than the self implemented one by about a factor of 2
    I suppose it does look a lot cleaner
    """
    @cache
    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)
    start_time = time.perf_counter_ns()
    fib(20)
    print(f"Built in Memo runtime: {(time.perf_counter_ns() - start_time) / 1000}ms")


def tabulation():
    def fib(n):
        # Initialise a list with the right length as a start
        dp = [0] * (n + 1)
    
        # Storing the independent values in dp
        dp[0] = 0
        dp[1] = 1
    
        # Using the bottom-up approach
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
    
        return dp[n]

    start_time = time.perf_counter_ns()
    fib(20)
    print(f"Tabulation runtime: {(time.perf_counter_ns() - start_time) / 1000}ms")


if __name__ == "__main__":
    brute_force()
    memoization()
    tabulation()
    built_in_memoization()
