# Python syntax means "the rules that define how Python code must be written."
# print("Hellotushar")

# a = 'Tushar'
# print("Hello" + a)

# def test():
#     d = "Tusharuty"
#     b ="babu"
#     c = a + d
#     return c
'''
📝 Summary

input() always gives a string

Use int() when you need to do comparisons or calculations

Names, emails, IDs = strings

Age, price, salary, marks = integers/floats
'''
#this is the example for the int


name = input("enter the name:")
age = int(input("enter the number: "))

if age > 18:
    print("Hello welcome Hero: ",age,name)
else:
    print("sorry dude you are restricted")

#This is the example for the float
temp = 12.5

if temp > 15:
    print("the temp is High: ",temp)
else:
    print("Low Temp: ",temp)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
balance = float(input("Enter account balance: "))
grade = input("Enter your grade (A/B/C): ")

if age >= 18:
    print(name, "is an adult")
else:
    print(name, "is a minor")

if balance > 1000.50:
    print("Sufficient balance")
else:
    print("Low balance")

if grade == "A":
    print("Excellent student")
else:
    print("Work hard")

