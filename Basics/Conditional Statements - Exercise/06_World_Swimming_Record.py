# 6. World Swimming Record
import math

worldRecord = float(input())
meters = float(input())
secondsPerMeter = float(input())

resistance = math.floor(meters / 15) * 12.5
swimmerTime = (secondsPerMeter * meters) + resistance

if swimmerTime < worldRecord:
    print(f'Yes, he succeeded! The new world record is {"%.2f" % swimmerTime} seconds.')
else:
    print(f'No, he failed! He was {"%.2f" % (swimmerTime - worldRecord)} seconds slower.')