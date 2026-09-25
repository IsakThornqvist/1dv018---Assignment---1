list_for_test = [9, 1, 8, 6, 5, 3, 4, 6, 10, 2, 7,]

class SortingAlgorithms:
    
    def selection_sort(self, lst):
        copy_of_list = lst.copy()

        for i in range(0, len(copy_of_list)):
            min_index = i
            for j in range(i + 1, len(copy_of_list)):
                if copy_of_list[j] < copy_of_list[min_index]:
                    min_index = j
            copy_of_list[i], copy_of_list[min_index] = copy_of_list[min_index], copy_of_list[i]

        return copy_of_list



    def bubble_sort(self, lst):
        copy_of_list = lst.copy()

        for i in range(0, len(copy_of_list) -1):
            for j in range(0, len(copy_of_list) -1):
                if copy_of_list[j] > copy_of_list[j + 1]:
                    copy_of_list[j], copy_of_list[j + 1] = copy_of_list[j + 1], copy_of_list[j]
        return copy_of_list



    def insertion_sort(self, lst):
        copy_of_list = lst.copy()

        for i in range(1, len(copy_of_list)):

            insertion_value = copy_of_list[i]

            j = i - 1

            while j >= 0 and copy_of_list[j] > insertion_value:
                copy_of_list[j + 1] = copy_of_list[j]
                j -=  1

            copy_of_list[j + 1] = insertion_value

        return copy_of_list

    def merge_sort(self, lst):
        copy_of_list = lst.copy()

        if len(copy_of_list) <= 1:
            return copy_of_list

        middle = len(copy_of_list) // 2
        left = copy_of_list[:middle]
        right = copy_of_list[middle:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        sorted_list = []

        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list += [left[i]]
                i += 1
            else:
                sorted_list += [right[j]]
                j += 1

        while i < len(left):
            sorted_list += [left[i]]
            i += 1

        while j < len(right):
            sorted_list +=[right[j]]
            j += 1

        return sorted_list


    def quick_sort(self, lst):
        copy_of_list = lst.copy()

        if len(copy_of_list) <= 1:
            return copy_of_list

        pivot = copy_of_list[0]

        left = []
        right = []

        for i in range(1, len(copy_of_list)):
            value = copy_of_list[i]

            if value <= pivot:
                left += [value]
            else:
                right += [value]

        sorted_left = self.quick_sort(left)
        sorted_right = self.quick_sort(right)

        result = sorted_left + [pivot] + sorted_right

        return result

    def bucket_sort(self, lst):
        copy_of_list = lst.copy()

        if not copy_of_list:
            return copy_of_list

        bucket = []
        smallest_value = min(copy_of_list)
        biggest_value = max(copy_of_list)

        if smallest_value == biggest_value:
            return copy_of_list

        for i in range(len(copy_of_list)):
            bucket.append([])

        for value in copy_of_list:
            bucket_index = int((value - smallest_value) / (biggest_value - smallest_value) * (len(bucket) - 1))

            bucket[bucket_index].append(value)

        for current_bucket in bucket:
            current_bucket.sort()

        result = []

        for current_bucket in bucket:
            for value in current_bucket:
                result.append(value)

        return result
        
