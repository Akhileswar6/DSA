def threeSumClosest(nums, target):
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            curr = nums[i] + nums[left] + nums[right]

            if abs(curr - target) < abs(closest - target):
                closest = curr

            elif curr < target:
                left += 1
            elif curr > target:
                right -= 1

            else:
                return curr

    return closest

print(threeSumClosest([-1, 2,1,4], 1))