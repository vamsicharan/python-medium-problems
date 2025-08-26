numbers = [34, 88, 423, 121, 2382, 10]
count_num = 0

for num in numbers:
    last_digit = num % 10      # last digit
    
    # find first digit using division
    first_digit = num
    while first_digit >= 10:
        first_digit //= 10
    
    if first_digit == last_digit:
        count_num += 1

print(count_num)