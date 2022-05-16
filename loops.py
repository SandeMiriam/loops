#1 Print First 10 numbers using while loop
from tokenize import Number


numbers = 1
while(numbers<=10):
    print(numbers)
    numbers += 1

#2 print the following pattern
number=[]
for num in range (1,6):
    number.append(num)
    print (number)
 

#3Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
guess_number =int(input("Enter a number: "))
sum= guess_number*(guess_number+1)/2
print (sum)

#4 write a program to print multiplication table
n=3
p=1
for m in range(1,20):
    p=n*m
    print(p)


#5 Display numbers from a list using loop
#The number must be divisible by five
#If the number is greater than 150, then skip it and move to the next number
#If the number is greater than 500, then stop the loop

nums=[12,57,150,180,525,50]
for y in nums:
    if y >500:
        break
    elif y>150:
       continue
    elif y%5==0:
        print(y)
    