def containsDuplicates(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False

print(containsDuplicates([1,2,3,4,5,6,7]))