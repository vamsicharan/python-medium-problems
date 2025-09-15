# Find the First Non-Repeating Character

# Problem: Write a function to find the first non-repeating character in a string.
# Testcase 1:
# Input: "swiss"
# Output: 'w'

def char():
    name = "swiss"
    res = {}
    result = ""
    for i in name:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    for a,b in  res.items():
        if b == 1:
            result += a
    return result[0]
print(char()) 