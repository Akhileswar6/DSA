def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

print(singleNumber([1,2,3,2,1,3,4])) 