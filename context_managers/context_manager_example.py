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


if __name__ == "__main__":
    with ContextManager() as manager:
        print("\tPrinted from within the statement block")
        manager.extra_method_that_can_be_called()
