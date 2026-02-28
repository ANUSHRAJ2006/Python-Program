x=1000
i=100
while i<=x:
    j=2
    while j<i:
        if i%j==0:
            break
        j+=1
    else:
        print(i)
    i+=1
