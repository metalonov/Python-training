# 7. Shopping

budget = float(input())
gpuCount = int(input())
cpuCount = int(input())
memoryCount = int(input())

gpuPrice = 250
gpuValue = gpuCount * gpuPrice

cpuPrice = gpuValue * 0.35
memoryPrice = gpuValue * 0.1

totalValue = gpuValue + (cpuCount * cpuPrice) + (memoryCount * memoryPrice)

if gpuCount > cpuCount:
    totalValue = totalValue - (totalValue * 0.15)

if budget >= totalValue:
    print(f'You have {"%.2f" % (budget - totalValue)} leva left!')
else:
    print(f'Not enough money! You need {"%.2f" % (totalValue - budget)} leva more!')