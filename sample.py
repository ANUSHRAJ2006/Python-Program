for i in range(1000):
    x=rf "D:\Python\Python\sample{i}.txt"
    c=open(x,'w')
    c.write('Hello World')
    c.close()
print('done')    
