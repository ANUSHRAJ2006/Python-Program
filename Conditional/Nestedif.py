mark=int(input('Enter the mark:'))
if mark>90 and mark<=100:
    print('Choose Medical')
    if mark>95:
        print('Choose MBBS')
        if mark>98:
            print('Eye specilist')
        elif mark<=95:
            print('Choose Vednary')
elif mark<=90 and mark>70:
    print('Chooose Engineering')
    if mark>80:
        print('Choose IT/AIDS')
    elif mark>70 and mark<=80:
        print('Choose /civil/Mech')
elif mark<=70 and mark>=50:
    print('Choose Arts and Science')
elif mark>=35 and mark<50:
    print('Choose Diplamo/ITI')
else:
    print('You are not clear the exam')
    if mark<30:
        print('Try on next attempt')
    else:
        print('Try to get 5 mark to clear exam')
