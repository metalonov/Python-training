# 4. Toy Shop

tripPrice = float(input())
puzzlesQty = int(input())
dollsQty = int(input())
bearsQty = int(input())
minionsQty = int(input())
trucksQty = int(input())

allToysSold = puzzlesQty + dollsQty + bearsQty + minionsQty + trucksQty

moneyEarned = (((((puzzlesQty * 2.6) +
               (dollsQty * 3)) +
               (bearsQty * 4.1)) +
               (minionsQty * 8.2)) +
               (trucksQty * 2))

if allToysSold  >= 50 :
    moneyEarned -= moneyEarned * 0.25

moneyEarned -= moneyEarned * 0.1

if moneyEarned >= tripPrice :
    print(f'Yes! {"%.2f" % (moneyEarned - tripPrice)} lv left.')
else :
    print(f'Not enough money! {"%.2f" % (tripPrice - moneyEarned)} lv needed.')