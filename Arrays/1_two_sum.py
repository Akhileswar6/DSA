def two_Sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in seen:
            return[seen[diff], i]

        seen[nums[i]] = i

print(two_Sum([2,7,11,15],9))


# Brute Force
# def two_Sum(nums, target):

#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             total = nums[i] + nums[j]

#             if total == target:
#                 return [i,j]

# print(two_Sum([3,3,3],9))
