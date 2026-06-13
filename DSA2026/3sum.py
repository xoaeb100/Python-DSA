# 3 sum
def threesum(arr):
    res  = []
    arr.sort()

    for i, a in enumerate(arr):
        if i> 0 and a == arr[i-1] :
            continue

        l,r = i+1, len(arr) -1
        while l<r:
            targetValue = a + arr[l] + arr[r]
            if targetValue > 0:
                r-=1
            elif targetValue < 0:
                l+=1
            else:
                res.append([a,arr[l], arr[r]])
                l+=1
                while l<r and arr[l] == arr[l-1]:
                    l+=1
    return res

print(threesum([1,2,-1,0,2]))


        