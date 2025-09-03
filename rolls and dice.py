# cook your dish here
for _ in range(int(input())):
    X, Y = map(int, input().split())
    target = 50 - X
    if 2*Y <= target <= 2*(Y + 5):
        print("Yes")
    else:
        print("No")