def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            print(arr, arr[j], arr[j+1])

            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print("terjadi pertukaran")

        print("one loop done")

arr = [88, 18, 23, 10, 21, 77, 54]

bubbleSort(arr)

print ("Sorted array is:", *arr)