# ===============================
# Exercises: Level 1
# ===============================

# 1. Declare an empty list
lst=list()

# 2. Declare a list with more than 5 items
list_1=[23,501,56,45,9875,19,85]
# 3. Find the length of your list
print(len(list_1))
# 4. Get the first item, the middle item and the last item of the list
print(list_1[0])
#for calculating middle follow below process
middle=len(list_1)//2
print(list_1 [middle])
print(list_1[-1])
# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=['Karuna','19','256.7','no','India']
# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
# 7. Print the list using print()
print(it_companies)
# 8. Print the number of companies in the list
count=0
for word in it_companies:
    count+=1
print('count of the list is :',count)
# 9. Print the first, middle and last company
print(it_companies[0])
print(it_companies[-1])
# for middle it is wrong print(it_companies[3])
middle=len(it_companies)//2
print(it_companies[middle])

# 10. Print the list after modifying one of the companies
it_companies[2]='Oppo'
print(it_companies)
# 11. Add an IT company to it_companies
it_companies.append('Samsung')
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2,'Vivo')
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
new_it_companies=[word.upper() for word in it_companies]
print(new_it_companies)
# 14. Join the it_companies with a string '#;  '
result='#;'.join(it_companies)
print(result)
# 15. Check if a certain company exists in the it_companies list.
does_exist='Oppo' in it_companies
print(does_exist)
# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)
# 17. Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)

print(it_companies)
# 18. Slice out the first 3 companies from the list
print(it_companies[0:3])
# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])
# 20. Slice out the middle IT company or companies from the list
middle = len(it_companies)//2
print(it_companies[middle])
# 21. Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)
# 22. Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies)//2)
print(it_companies)
# 23. Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)
# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)
# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, 
# then insert Python and SQL after Redux.
full_stack=front_end.copy()
index = full_stack.index('Redux') + 1
full_stack.insert(index, 'Python')
full_stack.insert(index+1, 'SQL')

print(full_stack)