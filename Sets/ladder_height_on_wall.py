import math
length = float(input("Enter the length of ladder:- "))
angle = float (input("Enter the Angle form:- "))
height = length * math.sin(math.radians(angle))
print ("The height reached by the ladder on the wall:-", height," Feet")
