def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[x for x in arr if x < pivot]
    middle=[x for x in arr if x == pivot]
    right=[x for x in arr if x > pivot]
    print(f"Pivot:{pivot},Left:{left},Middle:{middle},Right:{right}")
    return quick_sort(left)+middle+quick_sort(right)
nums = list(map(int,input("enter elements").split()))
print("\nQuick Sort Result:",quick_sort(nums[:]))
