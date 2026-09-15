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

result_one_pointer = three_sum.threesum_pointer(first_list)
result_two_pointer = three_sum.threesum_pointer(second_list)
result_three_pointer = three_sum.threesum_pointer(third_list)


print("List 1")
print(first_list)
print("Brute", result_one)
print("Pointer", result_one_pointer)

print("List 2")
print(second_list)
print("Brute", result_two)
print("Pointer", result_two_pointer)

print("List 3")
print(third_list)
print("Brute", result_three)
print("Pointer", result_three_pointer)







