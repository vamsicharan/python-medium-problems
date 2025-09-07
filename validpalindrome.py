# valid palindrome

s = "A man, a plan, a canal: Panama"
res = ""
for i in s:
    if  not i.isspace() and   i.isalnum():
        res += i.lower()
result = res[::-1]        
if res == result:
    print("true")
else:    
    print("false")
print(res) 