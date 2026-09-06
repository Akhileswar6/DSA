def containDuplicates(nums):
    seen = list()

    for num in nums:
        if num in seen:
            return True
        seen.append(num)
    return False

print(containDuplicates([1, 2, 3, 4, 1]))


# Brute Force
# def containDuplicates(nums):

#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True

#     return False

# print(containDuplicates([1, 2, 1]))
