# 8. Lunch Break
import math

showName = input()
showLength = int(input())
lunchLength = int(input())

lunchTime = lunchLength / 8
restTime = lunchLength / 4

timeLeft = lunchLength - (lunchTime + restTime)

if timeLeft >= showLength :
    print(f'You have enough time to watch {showName} and left with {math.ceil(timeLeft - showLength)} minutes free time.')
else :
    print(f'You don\'t have enough time to watch {showName}, you need {math.ceil(showLength - timeLeft)} more minutes.')