import math

a = 234.01
b = 6
c = -27.01

# this will round up the int to the next highest int
# regardless of how close it is to the lower int
print("this is the ceil function output for ", a, " -> ", math.ceil(a))
# this will round down to the closest int, regardless of how close it is to the next
# highest int
print("this is the floor function output for ", a, " -> ", math.floor(a))

# factorial is the numbers from 0 to the digit all times by each other
# for 6 it would be 1*2*3*4*5*6 = 720
print("this is the factorial output for ", b, " ->  ", math.factorial(b))
# fabs jus returns the positive value of the int
print("this is the absolute value output for ", c, " -> ", math.fabs(c))
