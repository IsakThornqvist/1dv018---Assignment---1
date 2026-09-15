list_for_test = [1, 19, 29, 11, 23, 10, 27, -3, -5, 19, -22, 28, -16, 9, -23]


class ThreeSum:
    def __init__(self):
        pass

    def threesum_brute(self, lst, sum=0):
        result = []
        lst = sorted(lst)

        for i in range(0, len(lst)-2):
            for j in range(i + 1, len(lst)):
                for k in range(j + 1, len(lst)):
                    if lst[i] + lst[j] + lst[k] == sum:
                        triple = (lst[i], lst[j], lst[k])

                        if triple not in result:
                            result.append(triple)

        return result

    def threesum_pointer(self, lst, sum=0):
        result = []
        lst = sorted(lst)

        for i in range(0, len(lst)-2):
            left = i + 1
            right = len(lst) - 1
            while left < right:
                current_sum = lst[i] + lst[left] + lst[right]

                if current_sum == sum:
                    triple = (lst[i], lst[left], lst[right])
                    result.append(triple)
                    left = left + 1
                    right = right - 1

                elif current_sum < sum:
                    left = left + 1

                elif current_sum > sum:
                    right = right - 1

        return result
    

# three_sum = ThreeSum()
# result = three_sum.threesum_brute(list_for_test)
# print(result)
