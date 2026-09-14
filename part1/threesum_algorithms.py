list_for_test = [1, 19, 29, 11, 23, 10, 27, -3, -5, 19, -22, 28, -16, 9, -23]

class ThreeSum:
    def __init__(self):
        self.list = list_for_test
        # print(self.list)

        

    def threesum_brute(self, lst, sum=0):
        result = []
        lst.sort()

        for i in range(0, len(lst)-2):
            for j in range(i + 1, len(lst)):
                for k in range(j + 1, len(lst)):
                    if lst[i] + lst[j] + lst[k] == sum:
                        triple = (lst[i], lst[j], lst[k])

                        if triple not in result:
                            result.append(triple)

        return result


# three_sum = ThreeSum()
# result = three_sum.threesum_brute(list_for_test)
# print(result)


