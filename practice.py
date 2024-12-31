#random practice question 

#cube-calculator

a = float(input("Enter Your Number:"))
cube=a*a*a
print ("The Cube ",cube)

#ends-here

#code for printing table of entered value

num = int(input("Enter your number:"))

for i in range(1,11):
    table = 0 
    table = num*i

    print( table )

#ends-here

''' NOTE : in range the value of i will increase by one     we wanted to fix the value of one and increase other  '''



#practical 1 

# Calculator code

num1=float(input("Enter Your First Number:"))

num2=float(input("Enter Your Second Number:"))

print("Select The Action You Want To Perform :-")
print("Addiction - press 1")
print("Subtraction - press 2")
print("Division - press 3")
print("Multiplication - press 4")

opert= int(input("Enter Your Operation No:"))

if opert==1:
    add=num1+num2
    print ("Addition :",add)

elif opert==2:
    sub=num1-num2
    print("Subtraction :",sub)

elif opert==3:
    did=num1/num2
    print("Division :",did)

elif opert==4:
    mul=num1*num2
    print("Multiplication :",mul)   

else:
    print("Invalid Number , Can't Perform Any Opration :)")


#practical 2    

#swapping of numbers

a = float(input("Enter Your Number:"))
b = float(input("Enter Your Number:"))

print( " before swapping " )

print("Number 1:", a)
print("Number 2:", b)

print("After Swapping")

print(a)
print(b)

print("Number 1:",b)
print("Number 2:",a)


#practical 11 

#find factorial of any number 

num = int(input("Enter your number:"))
fact = 1 

if (num > 0):
    for i in range(1,num+1):
        fact = fact*i 
    print ("The factorial:", fact)

elif num==0:
    print("The factorial of 0 is 1")

else:
    print("Factorial of negative numbers doesn't exist.")

 
# there are two method to calculate area of triangle 

#simple formula - less precise maybe can give inaccurate answer 

#heron's formula - more precise will 100% give accurate answer

 

#practical 7

''' first method : simple formula '''

base = int(input("Enter base:"))
height = int(input("Enter base:"))

area = (1/2)*base*height

print ("Area of Triangle:",area )  



#practical 14

''' second method : heron's formula '''


side1 = int(input("Enter 1st side :"))
side2 = int(input("Enter 2nd side :"))
side3 = int(input("Enter 3rd side :"))
s = (side1 + side2 + side3)/2

h_area = (s*(s - side1)*(s - side2)*(s - side3))**(1/2)

print ("Area of Triangle:",h_area ) 



#practical 12 

def checkLeap(year):
    if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        print("It is a Leap Year.")
    
    else:
        print("It is not a Leap Year.")

year = int(input("Enter the year:"))
checkLeap(year)

#practical 16 

#nested functions

def outerFn(x):
    def innerFn(y):
        return x+y 
    return innerFn(15)

result = outerFn(5)
print (result)