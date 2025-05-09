def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]  # Swap 0 to the correct position
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1  # 1 is already in the correct position
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]  # Swap 2 to the correct position
            high -= 1  # Do not increment mid, because the swapped value needs to be checked

    return nums
