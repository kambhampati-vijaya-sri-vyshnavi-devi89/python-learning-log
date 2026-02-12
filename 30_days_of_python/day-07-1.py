# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies

n=len(it_companies)
print('the length of it_companies is :',n)
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
# Insert multiple IT companies at once to the set it_companies

new_it_companies_to_add={'paypal','openai','wipro'}
it_companies.update(new_it_companies_to_add)
print('it companies list after adding :',it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('Google')
print(it_companies)

# What is the difference between remove and discard

'''
remove() method removes if the item is there but if not there it will raise an error 
however, discard() method does not raise the error even if not the item in set 
'''

#-------------Exercises: Level 2---------------------
# Join A and B
C=A|B
print(C)
# Find A intersection B
print(A.intersection(B))


# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets

print(A.isdisjoint(B))
# Join A with B and B with A
D=A.union(B)
print(D)
E=B.union(A)
print(E)

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))



# Delete the sets completely

del A
del B



#------------------Exercises: Level 3 -----------------------------------------
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?

st=set(age)
length_of_set=len(st)
length_of_list=len(age)
if length_of_list==length_of_set:
    print("same length")
else:
    if length_of_list>length_of_set:
        print("length of list is bigger")
    else:
        print("length of set is bigger ")


# Explain the difference between the following data types: string, list, tuple and set

'''
string: 
->it iterates character by character 
->collection of characters only 
->modifiable
list:
->collection of different data types
->ordered
->modifiable
->can be empty
-> allow duplicates
tuple:
->collection of different data types
->ordered
->unmodifiable
set:
->collection of different datatypes
->unordered
->unmodifiable
->duplication not allowed

'''

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies

n=len(it_companies)
print('the length of it_companies is :',n)
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
# Insert multiple IT companies at once to the set it_companies

new_it_companies_to_add={'paypal','openai','wipro'}
it_companies.update(new_it_companies_to_add)
print('it companies list after adding :',it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('Google')
print(it_companies)

# What is the difference between remove and discard

'''
remove() method removes if the item is there but if not there it will raise an error 
however, discard() method does not raise the error even if not the item in set 
'''

#-------------Exercises: Level 2---------------------
# Join A and B
C=A|B
print(C)
# Find A intersection B
A.intersection(B)
print(A)

# Is A subset of B
A.issubset(B)

# Are A and B disjoint sets

A.isdisjoint(B)
# Join A with B and B with A
D=A.union(B)
print(D)
E=B.union(A)
print(E)

# What is the symmetric difference between A and B
A.symmetric_difference(B)



# Delete the sets completely

del A
del B



#------------------Exercises: Level 3 -----------------------------------------
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?

st=set(age)
length_of_set=len(st)
length_of_list=len(age)
if length_of_list==length_of_set:
    print("same length")
else:
    if length_of_list>length_of_set:
        print("length of list is bigger")
    else:
        print("length of set is bigger ")


# Explain the difference between the following data types: string, list, tuple and set

'''
# ======================================================
# Difference Between String, List, Tuple and Set
# ======================================================

# ----------------------
# 1️⃣ String
# ----------------------
# - Collection of characters
# - Ordered (has index positions)
# - Immutable (cannot be modified after creation)
# - Allows duplicate characters
# - Written inside single (' ') or double (" ") quotes
# - Supports indexing and slicing

# Example:
# name = "Python"


# ----------------------
# 2️⃣ List
# ----------------------
# - Collection of multiple data types
# - Ordered (index-based)
# - Mutable (can add, remove, or modify elements)
# - Allows duplicate values
# - Written using square brackets []
# - Supports indexing and slicing

# Example:
# lst = [1, "apple", 3.5]


# ----------------------
# 3️⃣ Tuple
# ----------------------
# - Collection of multiple data types
# - Ordered (index-based)
# - Immutable (cannot change after creation)
# - Allows duplicate values
# - Written using parentheses ()
# - Supports indexing and slicing

# Example:
# tp = (1, "apple", 3.5)


# ----------------------
# 4️⃣ Set
# ----------------------
# - Collection of unique elements
# - Unordered (no index positions)
# - Mutable (can add or remove elements)
# - Does NOT allow duplicate values
# - Written using curly braces {}
# - Does NOT support indexing

# Example:
# st = {1, 2, 3}


# ======================================================
# Quick Comparison Summary
# ======================================================

# String  -> Ordered, Immutable, Allows duplicates
# List    -> Ordered, Mutable, Allows duplicates
# Tuple   -> Ordered, Immutable, Allows duplicates
# Set     -> Unordered, Mutable, No duplicates


'''

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
sentence="I am a teacher and I love to inspire and teach people"
words=sentence.split()
unique_words=set(words)
print(len(unique_words))