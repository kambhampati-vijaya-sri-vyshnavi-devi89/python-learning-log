#Day 2: 30 Days of python programming
#variables

first_name='kakinada'
last_name='prakasam'
full_name='prakasam district'
country='India'
age=20
city='Guntur'
year=2026
is_married='Yes'
is_light_on=True
color,month,day='pink',2,'monday'

#checking type of my variables

print(type(is_light_on))
print(type(country))
print(type(day))

#finding length using len built in function

print(len(first_name))

num_one=5
num_two=4
total=num_one+num_two
print(total)
diff=num_one-num_two
print(diff)
product=num_one*num_two
print(product)
division=num_two/num_one
print(division)
mod=num_two%num_one
print(mod)
floor=num_one//num_two
print(floor)
power=num_one**num_two
print(power)

'''
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
'''

def area_of_circle(radius_of_circle):
    print("area of circle is :",3.14*radius_of_circle)

def circumference_of_circle(radius_of_circle):
    print("Circumference of circle is :",2*3.14*radius_of_circle)

radius_of_circle=int(input("give me radius of circle:"))
area_of_circle(radius_of_circle)
circumference_of_circle(radius_of_circle)

