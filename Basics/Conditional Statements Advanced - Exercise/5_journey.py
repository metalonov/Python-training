# 5. Journey
from math import acosh

budget = float(input())
destination = input()
accomodation_type = ""
location = ""
spending = 0

if 0 < budget <= 100 :
    location = "Bulgaria"
    if destination == "summer" :
        accomodation_type = "Camp"
        spending = budget * 0.3
    elif destination == "winter" :
        accomodation_type = "Hotel"
        spending = budget * 0.7
elif 100 < budget <= 1000 :
    location = "Balkans"
    if destination == "summer" :
        accomodation_type = "Camp"
        spending = budget * 0.4
    elif destination == "winter" :
        accomodation_type = "Hotel"
        spending = budget * 0.8
else :
    location = "Europe"
    accomodation_type = "Hotel"
    spending = budget * 0.9

print(f"Somewhere in {location}")
print(f"{accomodation_type} - {spending:.2f}")
