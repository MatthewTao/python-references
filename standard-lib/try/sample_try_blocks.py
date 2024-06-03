import traceback


def try_finally():
    """
    This makes it complete with the code in the finally block, but still finishes with exit code 1.
    Therefore, the error isn't handled and will still be raised
    """
    try:
        answer = 1 / 0
        print(answer)
    finally:
        print("calculation completed")


def dummy_function():
    """
    Just a function to create more layers
    """
    divide_by_zero()


def divide_by_zero(a=0):
    return 1 / a


def try_except():
    try:
        dummy_function()
    except Exception as e:
        print(f"{e}")  # division by zero
        print(f"{repr(e)}")  # ZeroDivisionError('division by zero')

        # This should put the whole traceback as a string into the variable
        # dummy_function > divide_by_zero > the specific line that contains the error
        traceback_str = traceback.format_exc()
        print(traceback_str)

        print("\n Same traceback with limit = -1")
        # Contains the last line of the traceback
        # Just the specific line that contains the error and the error
        traceback_str = traceback.format_exc(limit=-1)
        print(traceback_str)

        print("\n Same traceback with limit = 1")
        # Contains the first line of the traceback
        # Just the call to dummy_function and the error
        traceback_str = traceback.format_exc(limit=1)
        print(traceback_str)


if __name__ == "__main__":
    try_except()
