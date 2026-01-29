# Sorted & unsorted array
def two_Sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        diff = target - nums[i]
        
        if diff in seen:
            return[seen[diff],i]
        
        seen[nums[i]] = i

print(two_Sum([2,7,11,15],9))



