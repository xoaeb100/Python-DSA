# Keep non-zeroes at the front.

def nonZerosOnLeft(arr):
    left = 0

    for right in range(len(arr)):
        if arr[right]!=0:
            arr[left], arr[right] = arr[right], arr[left]
            left +=1
    return arr

print( nonZerosOnLeft([1,2,9,0,0,2,4,0]))