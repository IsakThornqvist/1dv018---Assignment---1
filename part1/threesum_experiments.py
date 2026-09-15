import random
import time
from threesum_algorithms import ThreeSum


def generate_random_list(n):
    result = []


    for i in range(n):
        result.append(random.randint(-10 * n, 10* n))

    return result

three_sum = ThreeSum()

sizes = [100, 200, 300, 400, 500]

print("--- Time test ---")
for n in sizes:
    test_list = generate_random_list(n)

    start = time.perf_counter()
    three_sum.threesum_brute(test_list)
    brute_time = time.perf_counter() - start

    start = time.perf_counter()
    three_sum.threesum_pointer(test_list)
    pointer_time = time.perf_counter() - start

    print("List Size =", n)
    print("Brute Time:", brute_time, "Seconds")
    print("Pointer Time:", pointer_time, "Seconds")
    print()


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
print(first_list)
print("Brute", result_one_brute)
print("Pointer", result_one_pointer)

print("List 2")
print(second_list)
print("Brute", result_two_brute)
print("Pointer", result_two_pointer)

print("List 3")
print(third_list)
print("Brute", result_three_brute)
print("Pointer", result_three_pointer)







