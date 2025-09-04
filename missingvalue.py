# Find Missing Number

# Problem: Given an array of consecutive numbers with one missing, find the missing number.
# Testcase 1:
# Input: [1, 2, 4, 5]
# Output: [3]
def number():
    a =  [1, 2, 4, 5]
    sumv = 0
    b = 0
    c = []
    for i in range(1,a[-1]+1):
        sumv +=i
    for i in a:
        b += i
    d = sumv - b
    c.append(d)
    return c
print(number()) 