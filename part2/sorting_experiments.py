from part2.sorting_algorithms import SortingAlgorithms
import random
import time
import math
import matplotlib.pyplot as graph

sorting_algorithms = SortingAlgorithms()

print("Currently running sorting experiments")

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


def lin_reg(x, y):
    input_length = len(x)
    sum_of_all_values_in_x = sum(x)
    sum_of_all_values_in_y = sum(y)

    times_itself = 0

    for i in range(0, len(x)):
        times_itself += x[i] * x[i]

    total_of_x_times_y = 0

    for i in range(0, len(y)):
        total_of_x_times_y += x[i] * y[i]

    numerator = (
        input_length * total_of_x_times_y
        - sum_of_all_values_in_x * sum_of_all_values_in_y
    )

    denominator = (
        input_length * times_itself
        - sum_of_all_values_in_x * sum_of_all_values_in_x
    )

    k = numerator / denominator

    average_of_x = sum_of_all_values_in_x / input_length
    average_of_y = sum_of_all_values_in_y / input_length

    m = average_of_y - k * average_of_x

    return m, k


def calculate_logarithms(numbers):
    result = []
    for i in range(0, len(numbers)):
        result.append(math.log(numbers[i]))

    return result


def calculate_regression_line(x, m, k):
    regression_y = []
    for i in range(0, len(x)):
        regression_y.append(m + k *x[i])

    return regression_y


log_x = calculate_logarithms(list_sizes)
log_y_selection = calculate_logarithms(average_times_selection)
log_y_bubble = calculate_logarithms(average_times_bubble)
log_y_insertion = calculate_logarithms(average_times_insertion)

m_selection, k_selection = lin_reg(log_x, log_y_selection)
m_bubble, k_bubble = lin_reg(log_x, log_y_bubble)
m_insertion, k_insertion = lin_reg(log_x, log_y_insertion)

regression_y_selection = calculate_regression_line(log_x, m_selection, k_selection)
regression_y_bubble = calculate_regression_line(log_x, m_bubble, k_bubble)
regression_y_insertion = calculate_regression_line(log_x, m_insertion, k_insertion)


graph.scatter(log_x, log_y_selection)
graph.plot(log_x, regression_y_selection, label=f"Regression line (selection), k = {k_selection:.3f}")
graph.scatter(log_x, log_y_bubble)
graph.plot(log_x, regression_y_bubble, label=f"Regression line (bubble), k = {k_bubble:.3f}")
graph.scatter(log_x, log_y_insertion)
graph.plot(log_x, regression_y_insertion, label=f"Regression line (insertion), k = {k_insertion:.3f}")
graph.xlabel("Log(Input size)")
graph.ylabel("Log(Execution time)")
graph.title("Log-log plots for O(n^2) algorithms")

graph.legend()
graph.grid()

graph.show()


merge_sort_first_run = run_experiment(sorting_algorithms.merge_sort)
merge_sort_second_run = run_experiment(sorting_algorithms.merge_sort)
merge_sort_third_run = run_experiment(sorting_algorithms.merge_sort)

average_times_merge = calculate_average_time(merge_sort_first_run, merge_sort_second_run, merge_sort_third_run)

quick_sort_first_run = run_experiment(sorting_algorithms.quick_sort)
quick_sort_second_run = run_experiment(sorting_algorithms.quick_sort)
quick_sort_third_run = run_experiment(sorting_algorithms.quick_sort)

average_times_quick = calculate_average_time(quick_sort_first_run, quick_sort_second_run, quick_sort_third_run)

bucket_sort_first_run = run_experiment(sorting_algorithms.bucket_sort)
bucket_sort_second_run = run_experiment(sorting_algorithms.bucket_sort)
bucket_sort_third_run = run_experiment(sorting_algorithms.bucket_sort)

average_times_bucket = calculate_average_time(bucket_sort_first_run, bucket_sort_second_run, bucket_sort_third_run)

radix_sort_first_run = run_experiment(sorting_algorithms.radix_sort)
radix_sort_second_run = run_experiment(sorting_algorithms.radix_sort)
radix_sort_third_run = run_experiment(sorting_algorithms.radix_sort)

average_times_radix = calculate_average_time(radix_sort_first_run, radix_sort_second_run, radix_sort_third_run)

log_x = calculate_logarithms(list_sizes)
log_y_merge = calculate_logarithms(average_times_merge)
log_y_quick = calculate_logarithms(average_times_quick)
log_y_bucket = calculate_logarithms(average_times_bucket)
log_y_radix = calculate_logarithms(average_times_radix)

m_merge, k_merge = lin_reg(log_x, log_y_merge)
m_quick, k_quick = lin_reg(log_x, log_y_quick)
m_bucket, k_bucket = lin_reg(log_x, log_y_bucket)
m_radix, k_radix = lin_reg(log_x, log_y_radix)

regression_y_merge = calculate_regression_line(log_x, m_merge, k_merge)
regression_y_quick = calculate_regression_line(log_x, m_quick, k_quick)
regression_y_bucket = calculate_regression_line(log_x, m_bucket, k_bucket)
regression_y_radix = calculate_regression_line(log_x, m_radix, k_radix)

graph.scatter(log_x, log_y_merge)
graph.plot(log_x, regression_y_merge, label=f"Regression line (merge), k = {k_merge:.3f}")
graph.scatter(log_x, log_y_quick)
graph.plot(log_x, regression_y_quick, label=f"Regression line (quick), k = {k_quick:.3f}")
graph.scatter(log_x, log_y_bucket)
graph.plot(log_x, regression_y_bucket, label=f"Regression line (bucket), k = {k_bucket:.3f}")
graph.scatter(log_x, log_y_radix)
graph.plot(log_x, regression_y_radix, label=f"Regression line (radix), k = {k_radix:.3f}")
graph.xlabel("Log(Input size)")
graph.ylabel("Log(Execution time)")
graph.title("Log-log plots for merge, quick, bucket and radix sort algorithms")

graph.legend()
graph.grid()

graph.show()

graph.plot(list_sizes, average_times_merge, label="Average time (Merge)", linestyle="None", marker="x")
graph.plot(list_sizes, average_times_quick, label="Average time (Quick)", linestyle="None", marker="*")
graph.plot(list_sizes, average_times_bucket, label="Average time (Bucket)", linestyle="None", marker="o")
graph.plot(list_sizes, average_times_radix, label="Average time (Radix)", linestyle="None", marker="s")

graph.xlabel("list sizes in range 2000 to 9000")
graph.ylabel("Average time of runs: Time (seconds)")
graph.title("Running times for Merge, Quick, Bucket and Radix Sort")
graph.legend()
graph.grid()

graph.show()