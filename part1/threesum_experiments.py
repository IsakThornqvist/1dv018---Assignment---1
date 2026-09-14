import random


def generate_random_list(n):
    result = []


    for i in range(n):
        result.append(random.randint(-10 * n, 10* n))

    return result

test = generate_random_list(15)
print(test)
