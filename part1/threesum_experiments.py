import random
import time
import math
import matplotlib.pyplot as graph
from part1.threesum_algorithms import ThreeSum

three_sum = ThreeSum()

print("Currently running threesum experiments")

def generate_random_list(n):
    random_list = []


    for i in range(n):
        random_list.append(random.randint(-10 * n, 10* n))

    return random_list


def time_measure(algorithm, test_list):
    start = time.perf_counter()
    algorithm(test_list)
    return time.perf_counter() - start


def run_experiment(algorithm):
    run_times = []

    for n in list_sizes:
        test_list = generate_random_list(n)
        time_run_takes = time_measure(algorithm, test_list)
        run_times.append(time_run_takes)

    return run_times


list_sizes = [220, 240, 280, 300, 320, 340, 360, 380, 400, 420, 460, 500, 540, 600, 800]

brute_times_first_run = run_experiment(three_sum.threesum_brute)
brute_times_second_run = run_experiment(three_sum.threesum_brute)
brute_times_third_run = run_experiment(three_sum.threesum_brute)

pointer_times_first_run = run_experiment(three_sum.threesum_pointer)
pointer_times_second_run = run_experiment(three_sum.threesum_pointer)
pointer_times_third_run = run_experiment(three_sum.threesum_pointer)


def calculate_average_time(run_one, run_two, run_three):
    average_times = []
    for i in range(0, len(list_sizes)):
        average_times.append(
            (run_one[i] + run_two[i] + run_three[i]) / 3)

    return average_times


average_times_all_brute_runs = calculate_average_time(
    brute_times_first_run,
    brute_times_second_run,
    brute_times_third_run

)
average_times_all_pointer_runs = calculate_average_time(
    pointer_times_first_run,
    pointer_times_second_run,
    pointer_times_third_run

)


graph.plot(list_sizes, average_times_all_brute_runs, label="Average time (Brute)")
graph.plot(list_sizes, average_times_all_pointer_runs, label="Average time (Pointer)")


graph.xlabel("Input size")
graph.ylabel("Time (seconds)")
graph.title("Three_sum brute/pointer average time (Figure 1a)")
graph.legend()

graph.show()



graph.plot(list_sizes, brute_times_first_run, label="Brute Run 1")
graph.plot(list_sizes, brute_times_second_run, label="Brute Run 2")
graph.plot(list_sizes, brute_times_third_run, label="Brute Run 3")
graph.plot(list_sizes, pointer_times_first_run, label="Pointer Run 1")
graph.plot(list_sizes, pointer_times_second_run, label="Pointer Run 2")
graph.plot(list_sizes, pointer_times_third_run, label="Pointer Run 3")


graph.xlabel("Input size")
graph.ylabel("Time (seconds)")
graph.title("Three_sum brute/pointer three runs each (Figure 1)")
graph.legend()

graph.show()


first_list = generate_random_list(15)
second_list = generate_random_list(15)
third_list = generate_random_list(15)

result_one_brute = three_sum.threesum_brute(first_list)
result_two_brute = three_sum.threesum_brute(second_list)
result_three_brute = three_sum.threesum_brute(third_list)

result_one_pointer = three_sum.threesum_pointer(first_list)
result_two_pointer = three_sum.threesum_pointer(second_list)
result_three_pointer = three_sum.threesum_pointer(third_list)

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

m, k = lin_reg(list_sizes, average_times_all_brute_runs)

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
log_y_brute = calculate_logarithms(average_times_all_brute_runs)

m_brute, k_brute = lin_reg(log_x, log_y_brute)

regression_y_brute = calculate_regression_line(log_x, m_brute, k_brute)

log_y_pointer = calculate_logarithms(average_times_all_pointer_runs)

m_pointer, k_pointer = lin_reg(log_x, log_y_pointer)

regression_y_pointer = calculate_regression_line(log_x, m_pointer, k_pointer)



graph.scatter(log_x, log_y_brute, label="Measured data (brute)")
graph.plot(log_x, regression_y_brute, label="Regression line (brute)")
graph.scatter(log_x, log_y_pointer, label="Measured data (pointer)")
graph.plot(log_x, regression_y_pointer, label="Regression line (pointer)")
graph.xlabel("log(Input size)")
graph.ylabel("log(Execution time)")
graph.title("Log-log plot of three sum with brute/pointer Figure (2b)")

graph.legend()
graph.grid()

graph.show()

