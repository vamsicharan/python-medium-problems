# Find the Longest Word

# Problem: Write a function to find the longest word in a string.
# Testcase 1:
# Input: "The quick brown fox jumps over the lazy dog"
# Output: "jumps"


# # print(result)
# long = {}
# for i in result:
#     if i not in long:
#         long[i] = len(i)
# print(long)
# word = ""
# max_val = 0
# for a,b in long.items():
#     if b > max_val:
#         max_val = b
#         word = a
# print(word)
name = "The quick brown fox jumps over the lazy dog"
result = name.split()                          # or
word = ""
max_val = 0
for i in result:
    if len(i) >= max_val:
        max_val = len(i)
        word = i
        
print(f"{word} with length of {max_val}")