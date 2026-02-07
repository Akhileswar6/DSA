def twoSum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]

        if s < target:
            left += 1
        elif s > target:
            right -= 1
        else:
            return [left + 1, right + 1]

print(twoSum([2,7,11,15],9))

