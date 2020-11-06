import copy

class MergeSort:

    def sort(self, arr):
        self.temp = [0] * len(arr)
        self._sort(arr, left=0, right=len(arr)-1)
        return arr

    def _sort(self, arr, left, right):
        if left == right:
            return

        middle = (right + left) // 2
        self._sort(arr, left=left, right=middle)
        self._sort(arr, left=middle+1, right=right)
        self._merge_halves(arr, left, middle, right)

    def _merge_halves(self, arr, left, middle, right):
        left_index = left
        right_index = middle+1
        temp_index = left

        while left_index <= middle and right_index <= right:
            if arr[left_index] <= arr[right_index]:
                # take left
                self.temp[temp_index] = arr[left_index]
                left_index += 1
            else:
                # take right
                self.temp[temp_index] = arr[right_index]
                right_index += 1

            temp_index += 1

        # copy reminder of either half
        for i in range(left_index, middle+1):
            self.temp[temp_index] = arr[i]
            temp_index += 1

        for i in range(right_index, right+1):
            self.temp[temp_index] = arr[i]
            temp_index += 1
            
        # copy back from temp to orig arr
        for i in range(left, right+1):
            arr[i] = self.temp[i]
