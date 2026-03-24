def bubble_sort(arr):
    print("Bubble Sort working steps:")
    n=len(arr)
    for i in range(n):
        print(f"\nPass {i+1}:")
        for j in range(0, n-i-1):
            print(f"Comparing {arr[j]} and {arr[j-1]}")
            if arr[j]>arr[j+1]:
                print(f"--> Swapping {arr[j]} and {arr[j+1]}")
                arr[j],arr[j+1]=arr[j+1],arr[j]
            print("Current list:",arr)
    return arr
nums=list(map(int,input("enter elements").split()))
print("\nBubble Sort Result:",bubble_sort(nums[:]))
