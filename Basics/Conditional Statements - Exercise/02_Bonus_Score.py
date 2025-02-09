# 2. Bonus Score

score = int(input())
bonus = int(0)

if score <= 100: bonus += 5
elif score > 100 and score <= 1000: bonus += score * 0.2
elif score > 1000: bonus += score * 0.1

if score % 2 == 0: bonus += 1
elif score % 5 == 0: bonus += 2

print(bonus)
print(score + bonus)