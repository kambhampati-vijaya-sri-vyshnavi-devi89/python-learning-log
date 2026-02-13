
'''
💻 Exercises: Day 8
Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries
'''

dog={}
dog['name']='Max'
dog['color']='black'
dog['breed']='orea'
dog['legs']='four'
dog['age']=12
print(dog)

student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 21,
    "marital_status": "Single",
    "skills": ["Python", "Data Analysis", "Public Speaking"],
    "country": "USA",
    "city": "New York",
    "address": "123 Main Street"
}

print(student)
print("length of the student dic:",len(student))
print(student['skills'])
print(type(student['skills']))
student["skills"].extend(['java','c++','database'])
print(student["skills"])
print(student.keys())
print(student.values())
student_items=list(student.items())
print(student_items)
del student['last_name']
print(student)

del dog