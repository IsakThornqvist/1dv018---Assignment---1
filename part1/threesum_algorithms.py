list_for_test = [1, 19, 29, 11, 23, 10, 27, -3, -5, 19, -22, 28, -16, 9, -23]

class ThreeSum:
    def __init__(self):
        self.list = list_for_test
        print(self.list)

        

    def threesum_brute(self):
        result = []
        self.list.sort()

        for i in range(0, len(self.list)-2):
            for j in range(i + 1, len(self.list)):
                for k in range(j + 1, len(self.list)):
                    if sum([self.list[i], self.list[j], self.list[k]]) == 0:
                        result.append([self.list[i], self.list[j], self.list[k]])

        return result


three_sum = ThreeSum()
result = three_sum.threesum_brute()
print(result)


