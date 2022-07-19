"""
#palindrome
n = 1441
temp = n
rev = 0
while(n>0):
    dig = n%10
    rev = (rev*10) + dig
    n = n//10
if(temp==rev):
    print("this is palindrome no.")
else:
    print("this is not a palindrome no.")"""
########################################################################################################################
"""
#factorial
x = int(input("Insert any number: "))
fact=1
while x > 1:
   fact *= x
   x -= 1
print("The result of factorial = ", fact)"""
########################################################################################################################
"""
# fibbonacci series
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))

print("fibbonacci series")
for i in range(1,10):
    print(fib(i),end=" ")"""
########################################################################################################################
"""
# Armstrong number
n = int(input("Enter a number: "))
sum = 0
temp=n
while n > 0:
   dig= n%10
   sum = sum + (dig ** 3)
   n=n//10
if temp == sum:
   print(temp,"is an Armstrong number")
else:
   print(temp,"is not an Armstrong number")"""
########################################################################################################################
"""
#calculator
choice = input("Enter operator to use:")
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
if choice == '+':
   ans=A+B
elif choice == '-':
   ans=A+B
elif choice == '*':
   ans=A+B
elif choice == '/':
   ans=A+B
else:
   print("Invalid input")

print("the answer is",ans)"""
########################################################################################################################
"""
#patterns
########################################################################################################################
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print(" ")

########################################################################################################################
for i in range(5):
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")

########################################################################################################################
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")

########################################################################################################################
x=0
for i in range(0,5):
    x+=1
    for j in range(0,i+1):
        print(x,end=" ")
    print(" ")

########################################################################################################################
for i in range(6,0,-1):
    for j in range(0, i - 1):
        print("* ", end="")
    print(" ")"""
########################################################################################################################
"""
#leap year
def CheckLeap(Year):
  if((Year % 400 == 0) or
     (Year % 100 != 0) and
     (Year % 4 == 0)):
    print("Given Year is a leap Year");
  else:
    print ("Given Year is not a leap Year")
Year = int(input("Enter the number: "))
CheckLeap(Year)"""
########################################################################################################################
"""
#prime no.
number = int(input("Enter any number:"))
if number>1:
    for i in range(2,number):
        if (number%i)==0:
            print(number, "is not prime number")
            break
    else:
            print(number, "is prime number")"""
########################################################################################################################
"""
# find Area in python
PI = 3.14
r = float(input("Enter the radius of a circle:"))
area = PI * r * r
print("Area of a circle = %.2f" %area)"""
########################################################################################################################
"""
#reverse a list
a=[5,"ram",10,"ravi",3]
a.reverse()
print(a)"""
########################################################################################################################
"""
# Program to find the sum of all elements in a list
numbers = [6, 5, 3, 8, 4, 2, 5, 6, 11]
sum = 0
for i in numbers:
    sum = sum + i
print("The sum is", sum)"""
########################################################################################################################
"""
#Average of list elements
numbers = [6, 5, 3, 8, 4, 2, 5, 6, 11]
sum = 0
for i in numbers:
    sum = sum + i
    avg = sum/len(numbers)

print("The average is", avg)"""
########################################################################################################################
"""
#Max of list
numbers = [6, 5, 3, 8, 4, 2, 5, 6, 11]
x = max(numbers)
print(x)"""
########################################################################################################################
"""
#Min of list
numbers = [6, 5, 3, 8, 4, 2, 5, 6, 11]
x = min(numbers)
print(x)"""
########################################################################################################################
"""
def grouping_dictionary(l):
    result = {}
    for k, v in l:
         result.setdefault(k, []).append(v)
    return result
colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print("Original list:")
print(colors)
print("\nGrouping a sequence of key-value pairs into a dictionary of lists:")
print(grouping_dictionary(colors))"""
########################################################################################################################
"""
a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
x = [{key:value} for (key , value) in zip(b,c)]
y=[{key:value} for key, value in zip(a,x)]
print(y)"""
#######################################################################################################################
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {1, 2, 3}

set3 = set1.intersection(set2)

if set3 == set2:
 print("set2:",set2,"is a subset of set1:",set1)
else:
 print("set2 not a subset of set1")
#######################################################################################################################
s1 = {"apple", "mango"}
s2 = {"mango", "orange"}
s3 = s1-s2
s4= s2-s1
s=s3|s4
print(s)
#######################################################################################################################
l=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
m=[]
for i in range(0,len(l)):
 if len(l[i])==0:
    continue
 else:
     m.append(l[i])
print(m)
########################################################################################################################
test_list = [(1, 4, 5), (7, 8), (2, 4, 10)]
print("The original list is : " + str(test_list))

sum = 0
for sub in test_list:
    for i in sub:
        sum = sum + i
res = sum / len(test_list)

print("The mean of tuple list is : " + str(res))
########################################################################################################################
import re
p= input("Input your password")
x = True
while x:
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")