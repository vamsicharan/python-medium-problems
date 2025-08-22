# strong number 

num=145
a=num
sum=0
while num>0:
    digit = num % 10
    fact = 1
    for i in range(1, digit+1):
        fact = fact * i
    sum = sum + fact
    num = num // 10
if sum == a :
    print(" strong")
else:
    print("no")