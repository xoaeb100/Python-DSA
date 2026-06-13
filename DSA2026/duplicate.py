nums = [1,5,2,7,2]

def containsDuplicate(nums):
    prevMap = {}
    isDuplicate = False
    for i , n in enumerate(nums):
        if n in prevMap:
            isDuplicate = True
            return isDuplicate
        else:
            prevMap[n] = i
    return isDuplicate

print(containsDuplicate(nums))


# alternate solutions

def containsDuplicate2(nums):
    mySet =  Set()
    for i in nums:
        if i in mySet:
            return True
        mySet.add(i)
    return False
    