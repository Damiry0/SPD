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

    return [[r_list[i], p_list[i], q_list[i]] for i in range(0, len(r_list))]


def schrage_pmtn(tasks):

    # Algorithm initialization
    Nn = tasks  # Set of unassigned tasks (loaded data)
    Ng = []  # Set of tasks ready to be scheduled, empty at the beginning
    t = min(Nn)[R]  # Auxiliary variable (time)
    task = []  # Task
    current_task = [0, 0, float('inf')]  # Current task on machine
    CMax = 0  # The maximum moment of the deadlines for the delivery of tasks

    while (len(Ng)) or (len(Nn)):  # Run until both sets are empty
        """ Search for the task with the shortest preparation time (R) among Nn,
        check if time (R) is less than or equal to time t
        and whether the set Nn is not empty """
        while (len(Nn)) and (min(Nn)[R] <= t):

            task = min(Nn)  # Assign the found task
            Ng.append(task)  # Move the task to Ng set
            Nn.pop(Nn.index(min(Nn)))  # Delete the found task from Nn set

            # If the found task has a greater delivery time (Q) than the one currently executing
            if task[Q] > current_task[Q]:
                # Calulate new execution time (P) for current task
                current_task[P] = t - task[R]
                t = task[R]  # Update time to found task preparation time (P)
                if current_task[P] > 0:  # Check if the current task is finished
                    Ng.append(current_task)  # If not, add them back to Ng set

        if not(len(Ng)):  # If the set Ng is empty
            t = min(Nn)[R]  # Update time moment
        else:  # If the set Ng is not empty
            # Find the job with the longest delivery time (Q)
            task = max(Ng, key=itemgetter(Q))
            # Delete the found task from Ng set
            Ng.pop(Ng.index(max(Ng, key=itemgetter(Q))))
            # Update current task
            current_task = task
            # Update the time moment with the execution time (P) of the found task
            t += task[P]
            # Update maximum delivery time of tasks
            CMax = max(CMax, t+task[Q])
   
    return CMax


def display_results(results, schrage_time):

    print(f"\nAverage elapsed time: {(schrage_time)/ITERATIONS}s")
    print(f"Average elapsed time: {((schrage_time)*10e3)/ITERATIONS}ms")
    print(f"Average elapsed time: {((schrage_time)*10e6)/ITERATIONS}ns\n")
    print(f"CMax value: {results}")


if __name__ == "__main__":

    tasks = load_data()
    schrage_start = timeit.default_timer()
    for i in range(ITERATIONS):
        results = schrage_pmtn(copy.deepcopy(tasks))
    shrage_end = timeit.default_timer()

    schrage_time = shrage_end - schrage_start

    display_results(results, schrage_time)
