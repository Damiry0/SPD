from operator import itemgetter
import timeit
import copy

ITERATIONS = 1  # Iterations of algorithm
R = 0
P = 1
Q = 2


def load_data():

    global quantity
    all_list = []

    try:
        data = open("Data/SCHRAGE1.DAT", "r")  # Open file with data
        quantity = data.readline()  # Get number of data
        for line in data:
            all_list.extend(  # Append the list of numbers to the result array
                [int(item)  # Convert each number to an integer
                 for item in line.split()  # Split each line of whitespace
                 ])
    finally:
        data.close()

    r_list = all_list[::3]  # R values
    p_list = all_list[1::3]  # P values
    q_list = all_list[2::3]  # Q values

    return [(r_list[i], p_list[i], q_list[i]) for i in range(0, len(r_list))]


def schrage(tasks):

    # Algorithm initialization
    Nn = tasks  # Set of unassigned tasks (loaded data)
    Ng = []  # Set of tasks ready to be scheduled, empty at the beginning
    t = min(Nn)[R]  # Auxiliary variable (time)
    sigma = []  # Partial order consisting of scheduled tasks
    task = ()  # Task
    CMax = 0  # The maximum moment of the deadlines for the delivery of tasks
    t_end_list = []  # List of task completion times

    while (len(Ng)) or (len(Nn)):  # Run until both sets are empty
        """ Search for the task with the shortest preparation time (R) among Nn,
        check if time (R) is less than or equal to time t
        and whether the set Nn is not empty """
        while (len(Nn)) and (min(Nn)[R] <= t):

            task = min(Nn)  # Assign the found task
            Ng.append(task)  # Move the task to Ng set
            Nn.pop(Nn.index(min(Nn)))  # Delete the found task from Nn set

        if not(len(Ng)):  # If the set Ng is empty
            t = min(Nn)[R]  # Update time moment
        else:  # If the set Ng is not empty
            # Find the job with the longest delivery time (Q)
            task = max(Ng, key=itemgetter(Q))
            # Delete the found task from Ng set
            Ng.pop(Ng.index(max(Ng, key=itemgetter(Q))))
            # To the partial order, add the found task with the longest (Q) from the Ng set
            sigma.append(task)
            # Update the time moment with the execution time (P) of the found task
            t += task[P]
            # Update maximum delivery time of tasks
            CMax = max(CMax, t+task[Q])
            t_end_list.append(t)

    # The order of execution of the tasks returned by the algorithm
    return (CMax, sigma, t_end_list)


def display_results(results, schrage_time):

    print(f"\nAverage elapsed time: {(schrage_time)/ITERATIONS}s")
    print(f"Average elapsed time: {((schrage_time)*10e3)/ITERATIONS}ms")
    print(f"Average elapsed time: {((schrage_time)*10e6)/ITERATIONS}ns\n")
    print(f"CMax value: {results[0]}")
    #print(f"Scheduled tasks: {results[1]}")
    #print(f"Task completion times: {results[2]}")


if __name__ == "__main__":

    tasks = load_data()

    schrage_start = timeit.default_timer()
    for i in range(ITERATIONS):
        results = schrage(copy.deepcopy(tasks))
    shrage_end = timeit.default_timer()

    schrage_time = shrage_end - schrage_start

    display_results(results, schrage_time)

