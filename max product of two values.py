# Find the Maximum Product of Two Elements

# Problem: Write a function to find the maximum product of two elements in an array.
# Testcase 1:
# Input: [3, 5, -2, 8, 11] 
# Output: 8 * 11 → 88
def maximum():
    value =  [3, 5, 12, 8, 11] 
    max1 = value[0]
    max2 = value[1]
    if max1 > max2:
        max1 = value[0]
        max2 = value[1]
    else:
        max1 = value[1]
        max2 = value[0]
    for i in range(2,len(value)):
         if value[i] > max1:
             max2 = max1
             max1 = value[i]
         elif value[i] > max2 and  max2 != max1:
             max2 = value[i]
    product = max1 * max2
    print(product)
maximum()
