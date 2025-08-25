# harshad number
num=21
a=num
sum =0
while num>0:
    digit = num % 10
    sum += digit 
    num //= 10
if a % sum ==0 :
    print("harsad")
else:
    print("no")