from sorting_algorithms import SortingAlgorithms
import random
import time
import math
import matplotlib.pyplot as graph

sorting_algorithms = SortingAlgorithms()

list_sizes = [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

def generate_random_list(n):
    random_list = []


    for i in range(n):
        random_list.append(random.randint(-10 * n, 10* n))

    return random_list


def time_measure(algorithm, test_list):
    start = time.perf_counter()
    algorithm(test_list)
    return time.perf_counter() - start

test_lists = []

for n in list_sizes:
    test_lists.append(generate_random_list(n))

def run_experiment(algorithm):
    run_times = []

    for test_list in test_lists:
        time_run_takes = time_measure(algorithm, test_list)
        run_times.append(time_run_takes)

    return run_times


selection_sort_first_run = run_experiment(sorting_algorithms.selection_sort)
selection_sort_second_run = run_experiment(sorting_algorithms.selection_sort)
selection_sort_third_run = run_experiment(sorting_algorithms.selection_sort)
bubble_sort_first_run = run_experiment(sorting_algorithms.bubble_sort)
bubble_sort_second_run = run_experiment(sorting_algorithms.bubble_sort)
bubble_sort_third_run = run_experiment(sorting_algorithms.bubble_sort)
insertion_sort_first_run = run_experiment(sorting_algorithms.insertion_sort)
insertion_sort_second_run = run_experiment(sorting_algorithms.insertion_sort)
insertion_sort_third_run = run_experiment(sorting_algorithms.insertion_sort)

def calculate_average_time(run_one, run_two, run_three):
    average_times = []
    for i in range(0, len(list_sizes)):
        average_times.append(
            (run_one[i] + run_two[i] + run_three[i]) / 3)

    return average_times


average_times_selection = calculate_average_time(
    selection_sort_first_run,
    selection_sort_second_run,
    selection_sort_third_run

)
average_times_bubble = calculate_average_time(
    bubble_sort_first_run,
    bubble_sort_second_run,
    bubble_sort_third_run

)
average_times_insertion = calculate_average_time(
    insertion_sort_first_run,
    insertion_sort_second_run,
    insertion_sort_third_run

)

graph.plot(list_sizes, average_times_selection, label="Average time (Selection)", linestyle="None", marker="x")
graph.plot(list_sizes, average_times_bubble, label="Average time (Bubble)", linestyle="None", marker="o")
graph.plot(list_sizes, average_times_insertion, label="Average time (Insertion)", linestyle="None", marker="*")



graph.xlabel("list sizes in range 2000 to 9000")
graph.ylabel("Average time of runs: Time (seconds)")
graph.title("Running times for O(n^2) algorithms")
graph.legend()
graph.grid()

graph.show()
