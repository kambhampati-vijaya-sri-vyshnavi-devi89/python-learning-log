# Exercises - Day 3


# =========================================
# 1. Declare your age as an integer variable
# =========================================
age=20

# =========================================
# 2. Declare your height as a float variable
# =========================================
my_height=22.3

# =========================================
# 3. Declare a variable that stores a complex number
# =========================================
complex_number=2+5j
# =========================================
# 4. Prompt the user to enter base and height of a triangle
#    Calculate the area (area = 0.5 * base * height)
#
#    Example:
#    Enter base: 20
#    Enter height: 10
#    The area of the triangle is 100
# =========================================
base=int(input("enter the base of the triangle:"))
height=int(input("enter the height of the triangle:"))
print("The area of the triangle is",base*height)


# =========================================
# 5. Prompt the user to enter side a, b, and c of a triangle
#    Calculate the perimeter (perimeter = a + b + c)
#
#    Example:
#    Enter side a: 5
#    Enter side b: 4
#    Enter side c: 3
#    The perimeter of the triangle is 12
# =========================================
side_a=int(input("enter the side a of triangle:"))
side_b=int(input("enter the side b of triangle:"))
side_c=int(input("enter the side c of triangle:"))
print("the perimeter of the triangle is:",side_a+side_b+side_c)


# =========================================
# 6. Get length and width of a rectangle using input
#    Calculate area (area = length * width)
#    Calculate perimeter (perimeter = 2 * (length + width))
# =========================================
rec_length=int(input("enter the length of the rectangle:"))
rec_width=int(input("enter the width of the rectangle:"))
print("the perimeter of the rectangle is :",2*(rec_length+rec_width))


# =========================================
# 7. Get radius of a circle using input
#    Calculate:
#    - Area (area = pi * r * r)
#    - Circumference (c = 2 * pi * r)
#    Use pi = 3.14
# =========================================
radius_of_circle=int(input('enter the radius'))
print('Area of the circle:',3.14*radius_of_circle)
print('circumference of the circle:',2*3.14*radius_of_circle)

# =========================================
# 8. Calculate the slope, x-intercept, and y-intercept
#    of the equation: y = 2x - 2
# equation form-->y=mx+b
# =========================================
# Equation: y = 2x - 2

m = 2          # slope
b = -2         # y-intercept

# y-intercept
y_intercept = b

# x-intercept (when y = 0)
x_intercept = -b / m

print("Slope:", m)
print("Y-intercept:", y_intercept)
print("X-intercept:", x_intercept)




# =========================================
# 9. Find the slope and Euclidean distance
#    between points (2, 2) and (6, 10)
#    Slope formula: (y2 - y1) / (x2 - x1)
# =========================================
import math

x1, y1 = 2, 2
x2, y2 = 6, 10

slope = (y2 - y1) / (x2 - x1)
print("slope:", slope)

euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("euclidean distance is:", euclidean_distance)





# =========================================
# 10. Compare the slopes in task 8 and task 9
# =========================================
print('comparison of slopes in task8 and task9',m is slope)

# =========================================
# 11. Calculate the value of y (y = x^2 + 6x + 9). 
# Try to use different x values and figure out at what x value y is going to be 0.
# =========================================
"""
x=1
while True:
    y=x**2+6*x+9
    
    if y==0:
        print('x is ',x)       this is correct but logic is wrong for the given equation ,if we keep -3 in equation then only we get y=0
        break
    x+=1
"""
for x in range(-11,10):
    y=x**2+6*x+9
    if y==0:
        print('x is',x)
# =========================================
# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# =========================================

print(len('python'))
print(len('dragon'))
print("falsy comparison statement:",len('python')is not len('dragon'))


# =========================================
# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
# =========================================

print('on in python and dragon:','on' in'python' and 'on' in 'dragon' )

# =========================================
# 14. Check if 'jargon' is in the sentence:
#     "I hope this course is not full of jargon"
# =========================================
print ( 'is jargon is in the sentence -I hope this course is not full of jargon:','jaron' in 'I hope this course is not full of jargon')


# =========================================
# 15. Check if there is no 'on' in both
#     'dragon' and 'python'
# =========================================

print('Check if there is no on in both  dragon and python:','on' not in'python' and 'on' not in 'dragon' )

# =========================================
# 16. Find the length of the word 'python'
#     Convert it to float, then to string  ✅ len() always returns an integer (int)
# =========================================
a='python'
print('length of python:',len(a))
b=float(len(a))
print(b)
c=str(len(a))
print(c)

# =========================================
# 17. Check if a number is even
#     (Even numbers are divisible by 2 with remainder 0)
# =========================================
num=int(input('enter the number to check if given num is even or not:'))
if num%2==0:
    print(num,'it is even number')
else:
    print(num,'not a even number')
# =========================================
# 18. Check if floor division of 7 by 3
#     is equal to int converted value of 2.7
# =========================================
floor_division=7//3
value=int(2.7)
print('floor value is equal to int converted value of 2.7:',floor_division is value)

# =========================================
# 19. Check if type of '10' is equal to type of 10
# =========================================
d='10'
e=10
print('Check if type of string type 10 is equal to type of 10:',type(d) is type(e))


# =========================================
# 20. Check if int('9.8') is equal to 10
# =========================================
"""
f=int('9.8')
g=10
print("Check if int('9.8') is equal to 10",f is g)   this is the one i wrote below are the mistakes in my code 

❌ Problem 1: int('9.8') is invalid
int('9.8')

This causes a ValueError ❌
Because int() cannot convert a string with a decimal point directly.

✅ Correct way (two-step conversion)
f = int(float('9.8'))

❌ Problem 2: Using is instead of ==
f is g

is checks object identity, not value.

You want to compare values, so use:

==

"""
f = int(float('9.8'))
g = 10

print("Check if int('9.8') is equal to 10:", f == g)


# =========================================
# 21. Prompt user to enter hours and rate per hour
#     Calculate weekly earning
#
#     Example:
#     Enter hours: 40
#     Enter rate per hour: 28
#     Your weekly earning is 1120
# =========================================

hours=int(input("enter the hours :"))
rate_per_hour=int(input("enter the rate per hour:"))
print("your weekly earnings :",hours*rate_per_hour)
# =========================================
# 22. Prompt user to enter number of years lived
#     Calculate number of seconds lived
#     Assume a person lives 100 years
#
#     Example:
#     Enter number of years you have lived: 100
#     You have lived for 3153600000 seconds
# =========================================
years=int(input('enter the no of years:'))
seconds=years*365*24*60*60
print('You have lived for',seconds,'seconds')

# =========================================
# 23. Display the following table
#
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
# =========================================

