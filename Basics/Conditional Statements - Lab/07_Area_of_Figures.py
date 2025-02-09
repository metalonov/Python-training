# 7. Area of figures
import math

shapeType = input()

if shapeType == "square":
    sides = float(input())
    print("%.3f" % (sides * sides))
elif shapeType == "rectangle":
    side1 = float(input())
    side2 = float(input())
    print("%.3f" % (side1 * side2))
elif shapeType == "circle":
    radius = float(input())
    print("%.3f" % (math.pi * radius ** 2))
elif shapeType == "triangle":
    side = float(input())
    height = float(input())
    print("%.3f" % (side * height / 2))