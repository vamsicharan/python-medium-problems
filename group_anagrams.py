# Group Anagrams

# Problem: Write a function to group anagrams from an array of strings.
# Testcase 1:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
a = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = {}
for i in a:
    temp = "".join(sorted(i))
    if temp in res:
        res[temp].append(i)
    else:
        res[temp] = [i]
result =[]
for key,value in res.items():
    result . append(value)
print(result)  