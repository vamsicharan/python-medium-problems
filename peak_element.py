# Find Peak Element

# Problem: Write a function to find a peak element in an array. An element is a peak if it is not smaller than its neighbours.
# Testcase 1:
# Input: [1, 3, 20, 4, 1, 0]
# Output: 20
def values():
        nums = [1, 10, 2, 4, 3, 5]
        peak = 0
        for i in range(1,len(nums)-1):
            if  nums[i-1] < nums[i] > nums[i+1]:
                peak = nums[i]
        return peak
print(values()) 