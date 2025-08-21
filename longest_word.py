# 3.	Write a Python program to find the longest word in a sentence.
sentence = "Python is a powerful programming language"
result=sentence.split()
res={}
final=[]
for i in result:
    res[i]=len(i)
max_val=0
max_key="vamsi"
for a,j in res.items():
    if j > max_val:
        max_val = j  
        max_key = a
print(max_val,max_key) 