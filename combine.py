def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]  

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr

    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

arr = [88, 18, 23, 10, 21, 77, 54]

def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

n = len(arr)
quickSort(arr, 0, n-1)
print("Hasil QuickSort:", *arr)
arr = [88, 18, 23, 10, 21, 77, 54]
bubbleSort(arr)
print("Hasil BubbleSort:", *arr)