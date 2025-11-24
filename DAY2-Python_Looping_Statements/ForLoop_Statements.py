'''
🚀 Loops in Python – Complete Beginner to Advanced
⭐ What is a Loop?
A loop is used when you want to execute a block of code multiple times automatically.
Example:If you want to print "Hello" 100 times, instead of writing print() 100 times, you use a loop.
🧠 Why Loops?
Loops help when:
You want to repeat tasks
Work with data one by one (lists, strings, etc.)
Process items until a condition stops
🔥 Types of Loops in Python
Python mainly has 2 types of loops:
for loop
while loop
And we also have loop control statements:
break
continue
pass
else (yes, loops also have an else!)
Let’s learn everything step by step.
1️⃣ FOR LOOP
The for loop is used when we know how many times we want to repeat something, or we want to iterate over a collection like:
list
tuple
string
range'''


for T in range(1,7):
    print(T)
#The above question this will in line by line numbers up to 1 to 6
n = 8
for K in range(n):
    #print("The Range of K for the n is: ",(K))
    print('*' * K)

#in the reverse order we can use like this
for K in reversed(range(1,8)):
    print('*' * K)

# Method 1: Simple and clear 
for Z in range(9, 0, -1):
    print('*' * Z)
    # print(T)
    
