import timeit
import copy
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from Schrage.schrage import schrage
from SchragePmtn.schrage_pmtn import schrage_pmtn
from operator import itemgetter

ITERATIONS = 1  # Iterations of algorithm
R = 0
P = 1
Q = 2

CMAX = 0
PI = 1
END_TIMES = 2


def load_data():
    global quantity
    all_list = []

    try:
        data = open("Data/SCHRAGE7.DAT", "r")  # Open file with data
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


def find_a(result, b):
    """Find value a.
    The closest task with the smallest possible index
    such that there are no downtime, breaks, gaps
    in the machine's operation between this task and the task b
    """
    for i in range(0, len(result[PI])):
        if ((result[PI][i][R] + sum(x[P] for x in result[PI][i:b + 1]) + result[PI][b][Q]) == result[CMAX]):
            return i
        else:
            return 1


def find_b(result):
    """Find value b.
    The farthest task with the largest index in the order,
    such that the sum of its completion time and its delivery time is equal to Cmax
    """
    for i in range(0, len(result[PI])):
        if ((result[END_TIMES][i] + result[PI][i][Q]) == result[CMAX]):
            return i


def find_c(result, a, b):
    """  Find value c.
    The farthest task with the largest possible index in the sequence (but only between tasks a and b),
    such that its delivery time is shorter than the b task delivery time.
    """
    c = -1
    for i in range(a, b + 1):
        if result[PI][i][Q] < result[PI][b][Q]:
            c = i
    if c != -1:
        return c
    else:
        return -1


def carlier(tasks):
    Ub = float('inf')

    # Calulate schrage
    schrage_results = schrage(copy.deepcopy(tasks))

    U = schrage_results[CMAX]

    if U < Ub:
        Ub = U

    # Find values for determining the critical block
    b = find_b(schrage_results)
    a = find_a(schrage_results, b)
    c = find_c(schrage_results, a, b)

    if c == -1:
        return U

    # Find values in the critical block
    r_min = min(schrage_results[PI][c + 1:b + 1], key=itemgetter(R))[R]
    q_min = min(schrage_results[PI][c + 1:b + 1], key=itemgetter(Q))[Q]
    sum_p = sum(x[P] for x in schrage_results[PI][c + 1:b + 1])

    # Save r previous value at c position
    r_prev = schrage_results[PI][c][R]

    # Replace r value at c position
    schrage_results[PI][c][R] = max(
        schrage_results[PI][c][R], r_min + sum_p)

    # Calculate schrage_pmtn
    Lb = schrage_pmtn(copy.deepcopy(schrage_results[PI]))

    if Lb < Ub:
        U = carlier(copy.deepcopy(schrage_results[PI]))
        Ub = U

    # Restore r_prev value at c position
    schrage_results[PI][c][R] = r_prev

    # Save q previous value at c position
    q_prev = schrage_results[PI][c][Q]

    # Replace q value at c position
    schrage_results[PI][c][Q] = max(
        schrage_results[PI][c][Q], q_min + sum_p)

    # Calculate schrage_pmtn
    Lb = schrage_pmtn(copy.deepcopy(schrage_results[PI]))

    if Lb < Ub:
        U = carlier(copy.deepcopy(schrage_results[PI]))
        Ub = U

    # Restore q_prev value at c position
    schrage_results[PI][c][Q] = q_prev

    return U


def display_results(results, carlier_time):
    print(f"\nAverage elapsed time: {(carlier_time) / ITERATIONS}s")
    print(f"Average elapsed time: {((carlier_time) * 10e3) / ITERATIONS}ms")
    print(f"Average elapsed time: {((carlier_time) * 10e6) / ITERATIONS}ns\n")
    print(f"CMax value: {results}")
    # print(f"Scheduled tasks: {results[1]}")
    # print(f"Task completion times: {results[2]}")


if __name__ == "__main__":

    tasks = load_data()

    carlier_start = timeit.default_timer()
    for i in range(ITERATIONS):
        results = carlier(copy.deepcopy(tasks))
    carlier_end = timeit.default_timer()

    carlier_time = carlier_end - carlier_start

    display_results(results, carlier_time)