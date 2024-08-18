def misnum(nums):
    nums = list(set(nums))  # Remove duplicates
    n = len(nums)
    
    # Mark numbers out of range and non-positive numbers
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    
    def remove_nmu_bt_n(nums, n):
        for i in range(n):
            val = abs(nums[i])
            if val <= n:
                nums[val - 1] = -abs(nums[val - 1])
        
        # Find the first positive index
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1

    return remove_nmu_bt_n(nums, n)

nums = [0, 1,2, 3, 4, 5, 9, 10]
print(misnum(nums))
