import random
from threesum_algorithms import ThreeSum


def generate_random_list(n):
    result = []


    for i in range(n):
        result.append(random.randint(-10 * n, 10* n))

    return result

three_sum = ThreeSum()
first_list = generate_random_list(15)
second_list = generate_random_list(15)
third_list = generate_random_list(15)
result_one = three_sum.threesum_brute(first_list)
result_two = three_sum.threesum_brute(second_list)
result_three = three_sum.threesum_brute(third_list)
print(first_list)
print(result_one)
print(second_list)
print(result_two)
print(third_list)
print(result_three)
