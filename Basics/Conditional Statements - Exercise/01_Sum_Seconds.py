# 1. Sum Seconds

timeFirst = int(input())
timeSecond = int(input())
timeThird = int(input())

totalSeconds = timeFirst + timeSecond + timeThird

print(f"{totalSeconds // 60}:{(totalSeconds % 60):02d}")