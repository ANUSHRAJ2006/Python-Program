def num(n):
    if n==1 or n<=1:
        return n
    else:
        print(n)
        return num(n-1)
x=num(10)
print(x)
