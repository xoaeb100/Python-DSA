def bubbleSort(arr):
    n = len(arr)
    swapped =True
    while swapped:
        swapped = False
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                arr[i] , arr[i+1]= arr[i+1],arr[i]
                swapped = True

        n=n-1
    return arr


myArr= [3,6,2,8,8,9,1]
print(bubbleSort(myArr))