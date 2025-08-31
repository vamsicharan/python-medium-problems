# intersection_of_arrays_dict.py

def intersection(arr1, arr2):
    freq = {}
    result = []

    # Count elements of first array
    for num in arr1:
        freq[num] = freq.get(num, 0) + 1

    # Check elements of second array
    for num in arr2:
        if num in freq and freq[num] > 0:
            result.append(num)
            freq[num] -= 1

    return result


# Example
arr1 = [1, 2, 2, 3]
arr2 = [2, 2, 3, 4]

print("Intersection:", intersection(arr1, arr2))
