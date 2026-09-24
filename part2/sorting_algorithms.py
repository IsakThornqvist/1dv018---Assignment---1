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

