nums= [2,3,4,5,6,0,1]

def minNumber(nums):
    result = nums[0]
    l,r = 0, len(nums) -1

    for i in nums:
        if nums[l] < nums[r]:
            result = min (result, nums[l])
        mid = (l+r) // 2
        result = min(result, nums[mid])
        if nums[mid] >= nums [l]:
            l = mid+1
        else:
            r = mid-1
    return result

print(minNumber(nums))