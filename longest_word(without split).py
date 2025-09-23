# Find the Longest Word

# Problem: Write a function to find the longest word in a string.
# Testcase 1:
# Input: "The quick brown fox jumps over the lazy dog"
# Output: "jumps"

name  = "The quick brown fox jumps over the lazy doges"
res = ""
word = ""
for i in name:
    if i != " ":
        word += i 
        if len(word) >= len(res):
            res = word
    else:
        word = ""
print(res) 