# 4. Fishing Boat

lease = 0

budget = float(input())
season = input()
people_count = int(input())


if season == "Spring" :
    lease = 3000
elif season == "Summer" or season == "Autumn" :
    lease = 4200
else :
    lease = 2600

if 0 < people_count <= 6 :
    lease -= lease * 0.1
elif 7 <= people_count <= 11 :
    lease -= lease * 0.15
else :
    lease -= lease * 0.25

if people_count % 2 == 0 and season != "Autumn" :
    lease -= lease * 0.05

if budget >= lease :
    print(f"Yes! You have {budget - lease:.2f} leva left.")
else :
    print(f"Not enough money! You need {lease - budget:.2f} leva.")