path=r'C:\Users\2006a\OneDrive\Documents\Book99.xlsx'
x=open(path,'r')
j=x.readline()
j=j.split(',')
for i in j:
    print(j)
