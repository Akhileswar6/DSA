def twoSum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else:
            return [left + 1, right + 1]
        
print(twoSum([2,3,5,7],12))
    
    
# Brute Force
# def twoSum(nums, target):

#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             total = nums[i] + nums[j]
#             if total == target:
#                 return [i+1, j+1]

# print(twoSum([2,7,11,15],9))