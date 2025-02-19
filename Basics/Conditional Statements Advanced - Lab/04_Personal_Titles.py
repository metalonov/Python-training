# 4. Personal Titles

enterAge = float(input())
enterGender = input()

if enterGender == "m" and enterAge >= 16 : 
	print("Mr.")
elif enterGender == "m" and enterAge < 16 : 
	print("Master")
elif enterGender == "f" and enterAge >= 16 :
	print("Ms.")
elif enterGender == "f" and enterAge < 16 :
	print("Miss")
else :
	print("incorrect data")