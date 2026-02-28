age=int(input("Enter the age:"))
if age>=18:
    print('you can watch any movies')
elif age<13 and age>0:
    print('you can watch kids movies')
elif age>=13:
    print('you can watch u/a certified movies')
else:
    print('age is not valid')
        
