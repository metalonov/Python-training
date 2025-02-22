# 3. New House

flower_price = 0

flower_type = input()
flower_count = int(input())
budget = float(input())

if flower_type == "Roses" :
    flower_price = 5
elif flower_type == "Dahlias" :
    flower_price = 3.8
elif flower_type == "Tulips" :
    flower_price = 2.8
elif flower_type == "Narcissus" :
    flower_price = 3
elif flower_type == "Gladiolus" :
    flower_price = 2.5

cost = flower_count * flower_price

if flower_count > 80 and flower_type == "Roses" :
    cost -= cost * 0.1
elif flower_count > 90 and flower_type == "Dahlias" :
    cost -= cost * 0.15
elif flower_count > 80 and flower_type == "Tulips" :
    cost -= cost * 0.15
elif flower_count < 120 and flower_type == "Narcissus" :
    cost += cost * 0.15
elif flower_count < 80 and flower_type == "Gladiolus" :
    cost += cost * 0.2

if cost <= budget :
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - cost:.2f} leva left.")
else :
    print(f"Not enough money, you need {cost - budget:.2f} leva more.")