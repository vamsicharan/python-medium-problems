# Longest Increasing subsequence in an array.
# Testcase 1:
# Input: [10, 9, 2, 5, 3, 7, 101, 18]
# Output: 4

def sub(lis):
    max_count = 0
    for i in range(len(lis)):
        count = 0
        for j in range(i+1, len(lis)):
            if lis[i] < lis[j]:
                count += 1
        # update max_count after checking each i
        if count > max_count:
            max_count = count
    return max_count

print(sub([10, 9, 2, 5, 3, 7, 101, 18]))
  