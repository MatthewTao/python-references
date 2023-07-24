"""
1) Arrive at the theater, get in line, and wait to purchase a ticket.
2) Buy a ticket from the box office.
3) Wait in line to have the ticket checked.
4) Get the ticket checked by an usher.
5) Choose whether or not to get in line for the concession stand:
    * If they get in line, then they purchase food.
    * If they don’t get in line, then they skip to the last step.
6) Go find their seat.


Each step in the env is one minute
"""

import simpy
import random
import statistics


wait_times = []


class Theater(object):
    def __init__(self, env, num_cashiers, num_servers, num_ushers):
        self.env = env
        self.cashier = simpy.Resource(env, num_cashiers)
        self.server = simpy.Resource(env, num_servers)
        self.usher = simpy.Resource(env, num_ushers)


    def purchase_ticket(self, moviegoer):
        # print(f'{moviegoer} purchased a ticket')
        yield self.env.timeout(random.randint(1, 3))

    def check_ticket(self, moviegoer):
        # print(f'{moviegoer} had their ticket checked')
        yield self.env.timeout(3 / 60)

    def sell_food(self, moviegoer):
        # print(f'{moviegoer} purchased some food')
        yield self.env.timeout(random.randint(1, 5))


def go_to_movies(env, moviegoer, theater: Theater):
    """
    This funtion describes and models the process of a movie goer
    """
    # Moviegoer arrives at the theater
    arrival_time = env.now
    # print(f'{moviegoer} arrives at {arrival_time}')

    with theater.cashier.request() as request:
        yield request # This causes the movie goer to wait for an available cashier
        
        # When cashier is available, go through the purchase ticket process
        yield env.process(theater.purchase_ticket(moviegoer))

    with theater.usher.request() as request:
        yield request
        yield env.process(theater.check_ticket(moviegoer))

    # Can maybe do a skewed choice
    if random.choice([True, False]):
        with theater.server.request() as request:
            yield request
            yield env.process(theater.sell_food(moviegoer))

    # Moviegoer heads into the theater
    wait_times.append(env.now - arrival_time)


def run_theater(env, num_cashiers, num_servers, num_ushers):
    """
    This function actually executes the simulation
    """
    theater = Theater(env, num_cashiers, num_servers, num_ushers)

    # The doors open, establish initial numbers
    for moviegoer in range(3):
        env.process(go_to_movies(env, moviegoer, theater))

    # Create a new movie goer every 12 seconds.
    # Gather and confirm whether that statistic is true
    while True:
        yield env.timeout(0.20)
        
        moviegoer += 1
        env.process(go_to_movies(env, moviegoer, theater))


def get_average_wait_time(wait_times):
    average_wait = statistics.mean(wait_times)
    return average_wait


def calculate_wait_time(wait_times):
    average_wait = get_average_wait_time(wait_times)
    # Pretty print the results
    minutes, frac_minutes = divmod(average_wait, 1)
    seconds = frac_minutes * 60
    return round(minutes), round(seconds)


def get_user_input():
    num_cashiers = input("Input # of cashiers working: ")
    num_servers = input("Input # of servers working: ")
    num_ushers = input("Input # of ushers working: ")
    params = [num_cashiers, num_servers, num_ushers]
    if all(str(i).isdigit() for i in params):  # Check input is valid
        params = [int(x) for x in params]
    else:
        print(
            "Could not parse input. The simulation will use default values:",
            "\n1 cashier, 1 server, 1 usher.",
        )
        params = [1, 1, 1]
    return params


def main():
    # Setup
    random.seed(42)
    num_cashiers, num_servers, num_ushers = get_user_input()

    # Run the simulation
    env = simpy.Environment()
    env.process(run_theater(env, num_cashiers, num_servers, num_ushers))
    env.run(until=90)

    # View the results
    mins, secs = calculate_wait_time(wait_times)
    print(
        "Running simulation...",
        f"\nThe average wait time is {mins} minutes and {secs} seconds.",
    )


if __name__ == '__main__':
    main()
