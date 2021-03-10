#This script calculates the age of the user corresponding to the next tenth.
print("To calculate how many years remain before the next decade, please enter your Name and age.")
#Interactive user input stored as string variables:
name = input("Enter your Name: ")
age = int(input("Enter your age: ")) #Age is a whole number, so it has to be defined as an integer, so we can make calculations.

#To get the last digit of age:
last_digit = age % 10 # with %, age is divided by 10 and the remainder is given = the last digit of a number

for years in range(0, 10):
    if (years + last_digit) == 10:
        print(name + ", in " + str(years) + " year/s you'll be " + str(age+years) + ".")

