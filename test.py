def moveZeros(nums):
    left = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1

    

        

    return nums

print(moveZeros(([1,0,1,1,1,0,0,0,1,0,1,1,0])))



    

        