# 3. Time + 15 minutes

hours = int(input())
minutes = int(input())

totalMinutes = minutes + 15

if totalMinutes >= 60:
    hours += 1
    totalMinutes -= 60
if hours >= 24:
    hours = 0


print(f"{hours}:{totalMinutes:02d}")