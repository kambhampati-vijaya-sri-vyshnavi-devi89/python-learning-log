# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

first='Thirty'
second='Days'
third='of'
fourth='python'
space=' '
final=first+space+second+space+third+space+fourth
print(final)


# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

a='Coding'
b='For'
c='All'
result=a+space+b+space+c
print(result)
print(" \n ")


# Declare a variable named company and assign it to an initial value "Coding For All".

company='coding for all'

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())


# Change all the characters to lowercase letters using lower() method.
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.title())
print(company.swapcase())
print(company.capitalize())
# Cut(slice) out the first word of Coding For All string.
print(company[0:6])
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('coding'))
print(company.index('coding'))
# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('coding','python'))
# Change "Python for Everyone" to "Python for All" using the replace method or other methods.

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
word='facebook,google,microsoft,apple,ibm,oracle,amazon'
print(word.split(','))
# What is the character at index 0 in the string Coding For All.
print(company[0])
# What is the last index of the string Coding For All.
print(len(company)-1)
# What character is at index 10 in "Coding For All" string.
print(company[10])
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = "Python For Everyone"

acronym = phrase[0] + phrase[7] + phrase[11]
print(acronym)

'''
# Create an acronym or an abbreviation for the name 'Python For Everyone'.

phrase = "Python For Everyone"
words = phrase.split()
acronym = ""

for word in words:
    acronym += word[0].upper()

print(acronym)

'''

# Create an acronym or an abbreviation for the name 'Coding For All'.
phrase1='Coding For All'
acronym1=phrase1[0]+phrase1[7]+phrase1[11]
# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('c'))
# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('f'))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
text = "Coding For All People"
print(text.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
# Use rindex to find the position of the last occurrence of the word because in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))
# Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])
'''
better way
start = sentence.find('because')
end = sentence.rfind('because') + len('because')
print(sentence[start:end])

'''
# Find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
# Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'

# Does 'Coding For All' start with a substring Coding?
print(company.startswith('coding'))

# Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.

new='      coding for all       '
print(new.strip())

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
e='30DaysOfPython'
f='thirty_days_of_python'
print(e.isidentifier())
print(f.isidentifier())
# The following list contains the names of some of python libraries:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

result = " # ".join(libraries)

print(result)

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('i am enjoying this challenge.\n i just wonder what is next')
# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki

print('Name\tAge \tCountry')
print('vijaya\t 19 \tIndia')



# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
print(formated_string)


# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) 
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))