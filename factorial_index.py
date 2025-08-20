# # Write a program that takes array of numbers as input and a number as second input.
# Check the position of the factorial of the second input number in the given array. Print the position of it.
# If the factorial of given second input number is not presented in the array then print factorial of  the number is not presented.
# # Testcase1	:  [ 61, 4, 6, 7, 120 , 10 ]
# # Input :  5
# # Output     	: 4

list_val =  [ 61, 4, 6, 7, 120 , 10 ]
num = int(input("enter num "))
fact=1
for i in range(1,num+1):
          fact *= i
for values in range(len(list_val)):
    if list_val[values] == fact :
        print(values)