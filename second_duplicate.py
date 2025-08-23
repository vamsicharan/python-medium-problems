# Write a program that takes array of numbers are input, print the second duplicate number and it’s occurrence.
case	=  [ 121, 8, 1, 4, 5, 4, 8, 1 ]
duplicates  = {}
sec=[]
for  i in range(len(case)):
    if case[i] not in duplicates:
        duplicates[case[i]]=1
    else:
        duplicates[case[i]]+=1
for a,b in duplicates.items():
    if b >= 2:
        sec.append(a)
print(sec[1])