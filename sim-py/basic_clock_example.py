import simpy
from simpy import Environment


def clock(env: Environment, name, tick):
    while True:
        print(name, env.now)
        yield env.timeout(tick)


if __name__ == "__main__":
    # Environment runs the simulation as fast as possible
    env = simpy.Environment()

    # Realtime Environment runs the step in inline with real time

    env.process(clock(env, "fast", 0.5))
    env.process(clock(env, "slow", 1))

    # Interesting that the step doesn't need to be an integer
    env.run(until=2.1)
