'''
Create an empty tuple
Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Join brothers and sisters tuples and assign it to siblings
How many siblings do you have?
Modify the siblings tuple and add the name of your father and mother and assign it to family_members
'''
tp1=tuple()
print(tp1)
sisters=('bob','alice','juliet','john')
brothers=('Muhammad','Oliver','Harry','Jack','George','Noah','Leo','Jacob')
siblings=sisters+brothers
print(siblings)
n=len(siblings)
print('the count of siblings:',n)


'''

⚠ Small Improvements
1️⃣ Question Clarity Issue

The question says:

Modify the siblings tuple and add the name of your father and mother and assign it to family_members

Technically, tuples are immutable.

So correct approach is either:

Option 1 (Better way without converting to list)
family_members = siblings + ('mom', 'dad')


This is cleaner and more Pythonic.

Your method works, but converting to list is not necessary here.
'''

siblings=list(siblings)
siblings.append('mom')
siblings.append('papa')
print(siblings)
siblings=tuple(siblings)
family_members=siblings
print("family members are :",family_members)