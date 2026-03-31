# Sorted & unsorted array
# Returns index values
def two_Sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        diff = target - nums[i]
        
        if diff in seen:
            return[seen[diff],i]
        
        seen[nums[i]] = i

print(two_Sum([2,7,11,15],9))



# Returns elements
def twoSum(nums, target):
    seen = set()
    for i in range(len(nums)):
        need = target - nums[i]
        if need in seen:
            return [need,nums[i]]

        seen.add(nums[i])
        
print(twoSum([2,7,11,15],9))




# Brute Force
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            
print(twoSum([2,7,11,15],9))


