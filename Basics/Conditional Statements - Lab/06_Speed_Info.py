# 6. Speed info

num = float(input())

if num <= 10: print('slow')
elif num > 10 and num <= 50: print('average')
elif num > 50 and num <= 150: print('fast')
elif num > 150 and num <= 1000: print('ultra fast')
else: print('extremely fast')
