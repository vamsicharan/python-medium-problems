# Convert the given Input Empty String into the given Output 
# Testcase 1: 
# Input : [ ] 
# Output : [[1,2,3][4,5,6][7,8,9]] 


result = []   # start with empty list
count = 1

for i in range(3):          # 3 sublists
    inner = []
    for j in range(3):      # each sublist has 3 numbers
        inner.append(count)
        count += 1
    result.append(inner)

print(result)