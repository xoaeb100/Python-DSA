nums = [1,5,-2,7,2]


def maxSubArray(nums):
    maxSum=nums [0]
    currSum = 0

    for i in nums:
        if currSum < 0:
            currSum = 0
        currSum = currSum +i
        maxSum = max(currSum, maxSum)
    return maxSum
print(maxSubArray(nums))
