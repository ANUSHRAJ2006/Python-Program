try:
    x=10/0
    print(x)
except Exception as e:
    print('your code have an error',e)
else:
    print('Everything done')
