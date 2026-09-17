import random
import time
import matplotlib.pyplot as graph
from threesum_algorithms import ThreeSum

three_sum = ThreeSum()

def generate_random_list(n):
    result = []


    for i in range(n):
        result.append(random.randint(-10 * n, 10* n))

    return result


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

print("--- Time test ---")

brute_times_first_run = run_experiment(three_sum.threesum_brute)
brute_times_second_run = run_experiment(three_sum.threesum_brute)
brute_times_third_run = run_experiment(three_sum.threesum_brute)

graph.plot(list_sizes, brute_times_first_run, label="Run 1")
graph.plot(list_sizes, brute_times_second_run, label="Run 2")
graph.plot(list_sizes, brute_times_third_run, label="Run 3")


graph.xlabel("Input size")
graph.ylabel("Time (seconds)")
graph.title("Three_sum brute force")
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

print("--- Correctness test ---")

print("List 1")
print("List to run algorithms on", first_list)
print("Brute", result_one_brute)
print("Pointer", result_one_pointer)

print("List 2")
print("List to run algorithms on", second_list)
print("Brute", result_two_brute)
print("Pointer", result_two_pointer)

print("List 3")
print("List to run algorithms on", third_list)
print("Brute", result_three_brute)
print("Pointer", result_three_pointer)







