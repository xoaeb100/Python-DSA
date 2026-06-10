nums = [1,5,-2,7,2]

def maxProductSubArray(nums):
    maxProd, minProd = 1,1
    result = max(nums)
    
    for i in nums:
        if i ==0:
            maxProd, minProd = 1,1
            continue
        temp =maxProd*i
        maxProd = max(maxProd *i, minProd*i, i)
        minProd = min(temp *i, minProd*i, i)
        result= max(maxProd, result)
    return result

print(maxProductSubArray(nums))


