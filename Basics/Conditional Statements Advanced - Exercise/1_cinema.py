# 1. Cinema

screening_type = input()
r = int(input())
c = int(input())

capacity = r * c

if screening_type == "Premiere" :
    print(f'{capacity * 12:.2f} leva')
elif screening_type == "Normal" :
    print(f'{capacity * 7.50:.2f} leva')
elif screening_type == "Discount" :
    print(f'{capacity * 5:.2f} leva')