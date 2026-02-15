def SumArray(arr):
    for i in range(1,len(arr)):
        arr[i] = arr[i] + arr[i - 1]

    return arr

print(SumArray([1,3,5,7,9,5,3,7]))