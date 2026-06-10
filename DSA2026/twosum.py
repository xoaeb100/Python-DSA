nums = [2,6,1,8,9]
target = 14

def twosum(nums, target):
    prevMap = {}
    
    for i,n in enumerate(nums):
        diff = target-n
        if diff in prevMap:
            return [prevMap[diff], i ]
        prevMap[n] = i
    return

print(twosum(nums, target))