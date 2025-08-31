#     *
#    ***
#   *****
#  1234567
# ABCDEFGHI


row=5
for i in range(1,row+1):
    a=97
    A=65
    print(" "*(row-i),end="")
    for j in range((i*2-1)):
        if i <=3:
            print("*",end="")
        elif i == 4:
            print(j+1,end="")
        else:
            print(chr(A),end="")
            A+=1
    print()  