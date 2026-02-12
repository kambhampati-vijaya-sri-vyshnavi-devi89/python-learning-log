#Unpack siblings and parents from family_members
family_members=('bob', 'alice', 'juliet', 'john', 'Muhammad', 'Oliver', 'Harry', 'Jack', 'George', 'Noah', 'Leo', 'Jacob', 'mom', 'papa')
*siblings,mother,father=family_members
print('siblings:',siblings)
print('mother:',mother)
print('father:',father)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits=('banana','apple','guava','pine apple','mango','orange')
vegetables=('potato','tomato','chilly','brianjal')
animal_products=('milk', 'eggs', 'cheese', 'honey', 'meat')
food_stuff_tp=fruits+vegetables+animal_products
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt=food_stuff_tp
print(food_stuff_lt)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

sorted_food = sorted(food_stuff_tp)

print(sorted_food)
n = len(sorted_food)

if n % 2 == 0:
    print("Middle items:",
          sorted_food[n//2 - 1],
          sorted_food[n//2])
else:
    print("Middle item:",
          sorted_food[n//2])

#Slice out the first three items and the last three items from food_stuff_lt list
print('the first 3 items from the list are :',food_stuff_lt[:3])
print('the last 3 items are :',food_stuff_lt[-3:])

# Delete the food_stuff_tp tuple completely
del food_stuff_tp


# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('if Estonia is a nordic country','Estonia' in nordic_countries)
print('Iceland is a nordic country','Iceland' in nordic_countries)

