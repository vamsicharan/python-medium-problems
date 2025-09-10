# Move Zeros to End  

# Problem: Write a function that moves all zeros in an array to the end while maintaining the order of other elements.
# Testcase 1:
# Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
def values():
    num =  [0, 1, 0, 3,0, 12]
    target = int(input("enter : "))
    a = []
    b = []
    for i in num:
        if i == target:
            a.append(i)
        else:
            b.append(i)
    return b+a        
print(values())