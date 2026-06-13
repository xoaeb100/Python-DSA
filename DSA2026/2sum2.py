# twosum2
def twoSum2(arr, target):
    l, r = 0 , len(arr)-1

    while l < r:
        if arr[l] + arr[r] > target:
            r -=1
        elif arr[l] + arr[r] < target:
            l +=1
        else:
            return [l+1, r+1]
    return []

print(twoSum2([1,2,5,6,10,15],12))
    