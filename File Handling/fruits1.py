f=open('fruit.txt','a')
f.write('Banana\n')
f.write('Orange\n')
f.close()

f=open('fruit.txt','r')
print(f.read())
