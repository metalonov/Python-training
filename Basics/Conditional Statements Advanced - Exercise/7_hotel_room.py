# 7. Hotel Room

discount = 0
studio_price = 0
flat_price = 0

month = input()
days = int(input())

if (month == "May") or (month == "October") :
    studio_price = 50 * days
    flat_price = 65 * days
    if 14 >= days > 7 :
        studio_price -= studio_price * 0.05
    elif days > 14 :
        studio_price -= studio_price * 0.3
        flat_price -= flat_price * 0.1
elif (month == "June") or (month == "September") :
    studio_price = 75.2 * days
    flat_price = 68.7 * days
    if days > 14 :
        studio_price -= studio_price * 0.2
        flat_price -= flat_price * 0.1
elif (month == "July") or (month == "August"):
    studio_price = 76 * days
    flat_price = 77 * days
    if days > 14 :
        flat_price -= flat_price * 0.1
else :
    print("error")

print(f"Apartment: {flat_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")