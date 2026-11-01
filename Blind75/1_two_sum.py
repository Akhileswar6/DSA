def twoSum(nums, target):
    seen = {}

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in seen:
            return[seen[diff], i]


        seen[nums[i]] = i


print(twoSum([2,7,9,11], 9))



def twoSum(nums, target):
    seen = []

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in seen:
            return[seen.index(diff), i]

        seen.append(nums[i])


print(twoSum([2,7,9,11], 9))