def twoSum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]

        if s < target:
            left += 1
        elif s > target:
            right -= 1
        else:
            return [left + 1, right + 1]
        
print(twoSum([2,3,5,7],12))
    
    
