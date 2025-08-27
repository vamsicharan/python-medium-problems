# abudent number
a=12
b=a
sum=0
for i in range(1,a):
    if a % i == 0:
        sum += i
if  sum > b:
    print("abudent")
else:
    print("no")