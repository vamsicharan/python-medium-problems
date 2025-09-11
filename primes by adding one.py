# # Write a program that takes array of numbers as input, among the numbers in array,
# print the numbers which forms a prime number by adding one to it. Print such numbers in the given array separated b spaces.
# # Testcase1	:  [ 7, 4, 7, 23, 10 ]
# # Output     	:  4 10

case= [ 7, 4, 7, 23, 10 ]

for i in range(len(case)):
        result = case[i]+1
        if result <2 :
            pass
        else:
            value = True
            for j in range(2,result):
                if result % j ==0:
                    value = False
                    break
            if value:
                print(case[i],end=" ")     