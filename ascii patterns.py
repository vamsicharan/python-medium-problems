row=5
for i in range(1,row+1):
    print(" "*(row-i),end="")
    for j in range(i):          # 0
        print(chr(65+j),end="")     # a
    for j in range(i-2,-1,-1):          # 
        print(chr(65+j),end="")   #  
         
    print() 