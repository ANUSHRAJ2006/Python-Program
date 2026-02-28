try:
    j=10
    print(j)
    x=10/0
    print(x)
except Exception as e:
    print('error',e)
finally:
    print('even thought if any error or no erroe\n I will work')
