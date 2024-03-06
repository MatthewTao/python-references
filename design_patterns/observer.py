"""
Use the observer pattern when changes to the state of one object requires changing other objects.
"""


class Subject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for obs in self._observers:
            obs.notify(self, *args, **kwargs)


class Observer:
    def __init__(self, observable, name):
        observable.register_observer(self)
        self.name = name

    def notify(self, observable, *args, **kwargs):
        print("Got", args, kwargs, "From", observable)
        self._some_action()

    def _some_action(self):
        print(f"{self.name} has been notified")


if __name__ == "__main__":
    subject = Subject()
    observer_1 = Observer(subject, "observer 1")
    observer_2 = Observer(subject, "observer 2")

    subject.notify_observers("test", kw="python")
