#printing nos from 1 to 10
for i in range(1,11):
    print(i)

# printing nos from 10 to 1 
for i in range(10,0,-1):  
    print(i)
"""
for printing from backwards we have to use negative step function
here 10=start
0=stop
-1= decrease by 1 for each iteration
"""
#print all even numbers from 1 to 20

for i in range(1,21):
    if i%2==0:
        print(i)

#print odd numbers from 1 to 100 
for i in range(1,101):
    if i%2!=0:
        print(i)

#print multiples of 5
for i in range(1,101):
    if 1%5==0:
        print(i)

#print the squares of numbers from 1 to 100

for i in range(1,101):
    print(i*i,end=" ")

#print all numbers from 1 to 15 but skip 5 
for i in range(1,15):
    if i==5:
        continue
    else:
        print(i)
    
#print all numbers from 1 to 15 and stop at 10
for i in range(1,16):
    if i==10:
        break
    else:
        print(i)

# count how many numbers are printing
count=0
for i in range(1,101):
    if i%2==0:
        print(i)
        count+=1

print("the count of numbers that are even from 1 to 100 are:",count)

