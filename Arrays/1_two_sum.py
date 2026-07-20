# # Sorted & unsorted array
# # Returns index values
def two_Sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        diff = target - nums[i]
        
        if diff in seen:
            return[seen[diff],i]
        
        seen[nums[i]] = i

print(two_Sum([2,7,11,15],9))



# # Returns elements
def twoSum(nums, target):
    seen = set()
    for i in range(len(nums)):
        need = target - nums[i]
        if need in seen:
            return [need,nums[i]]

        seen.add(nums[i])
        
print(twoSum([2,7,11,15],9))




def twoSum(nums, k):
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]
        if total < k:
            left += 1
        elif total > k:
            right -= 1
        else:
            return left, right

print(twoSum([7,9,12,15,18,20], 30))