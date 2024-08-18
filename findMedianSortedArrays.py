def FindMedianSortedArrays(nums1, nums2):
    i = 0
    j = 0
    n = 0
    number_of_elements = len(nums1) + len(nums2)
    median_rank = number_of_elements//2
    median = 0  
    while n <= median_rank:
        prev_number = median
        if i < len(nums1) and j < len(nums2):
            
            if nums1[i] <= nums2[j]:
                median = nums1[i]
                i +=1

            else:
                median = nums2[j]
                j +=1
        elif j < len(nums2):
            median = nums2[j]
            j+=1
        elif i < len(nums1):
            median = nums1[i]
            i+=1
        n+=1

    if number_of_elements % 2 == 1:
        return median
    else:
        return (median + prev_number)/2               

nums1 = [2]
nums2 = []

print(FindMedianSortedArrays(nums1, nums2))
