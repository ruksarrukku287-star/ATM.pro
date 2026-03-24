class Sort:
    def __init__(self, data):
        self.data = data

    def bubble_sort(self):
        arr = self.data[:]
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def selection_sort(self):
        arr = self.data[:]
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def insertion_sort(self):
        arr = self.data[:]
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

    def quick_sort(self, arr=None):
        if arr is None:
            arr = self.data[:]
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return self.quick_sort(left) + [pivot] + self.quick_sort(right)

    def merge_sort(self, arr=None):
        if arr is None:
            arr = self.data[:]
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            L = self.merge_sort(L)
            R = self.merge_sort(R)

            merged = []
            i = j = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    merged.append(L[i])
                    i += 1
                else:
                    merged.append(R[j])
                    j += 1
            merged.extend(L[i:])
            merged.extend(R[j:])
            return merged
        return arr


# Example usage
numbers = [64, 25, 12, 22, 11]
sorter = Sort(numbers)

print("Original:", numbers)
print("Bubble Sort:", sorter.bubble_sort())
print("Selection Sort:", sorter.selection_sort())
print("Insertion Sort:", sorter.insertion_sort())
print("Quick Sort:", sorter.quick_sort())
print("Merge Sort:", sorter.merge_sort())

        
