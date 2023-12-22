import functools
import operator


def function_example(a, b):
    print(f"a: {a}, b: {b}")
    return a + b


if __name__ == "__main__":
    # initializing list
    lis = [1, 3, 5, 6, 2]

    # using reduce to compute sum of list
    print("The sum of the list elements is : ", end="")
    print(functools.reduce(lambda a, b: a + b, lis))

    # using reduce to compute maximum element from list
    print("The maximum element of the list is : ", end="")
    print(functools.reduce(lambda a, b: a if a > b else b, lis))

    # using reduce to compute sum of list
    # using operator functions
    print("The sum of the list elements is : ", end="")
    print(functools.reduce(operator.add, lis))

    # using reduce to compute product
    # using operator functions
    print("The product of list elements is : ", end="")
    print(functools.reduce(operator.mul, lis))

    print(functools.reduce(function_example, lis))
