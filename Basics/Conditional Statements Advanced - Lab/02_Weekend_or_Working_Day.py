# 1. day of week

entry = input()

if entry == 'Monday' or entry == 'Tuesday' or entry == 'Wednesday' or entry == 'Thursday' or entry == 'Friday' :
    print('Working day')
elif entry == 'Saturday' or entry == 'Sunday' :
    print('Weekend')
else :
    print('Error')