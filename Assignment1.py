# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 22:34:34 2018

@author: Latha NV
"""

#Latha - First code - Assignment 1 - Problem 1  
#1. Install Jupyter notebook and run the first program and share the screenshot of the output.

q=5
s="Latha"
t=2.0
A=type(q)
B=type(s)
C=type(t)

print(A)
print(B)
print(C)

 

#Latha - First code - Assignment 1 - Problem 2
#2. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included). The numbers obtained should be printedin a comma-separated sequence on a single line.


result=[]
for x in range(2000, 3201):
    if x%7 == 0 and x%5!= 0:
        result.append(x)
        
print("Result = " + str(result))
 

#Latha - First code - Assignment 1 - Problem 3
#3. Write a Python program to accept the user's first and last name and then getting them printed
# in the reverse order with a space between first name and last name.

Fname= input("Enter the First Name :" )
Lname= input("Enter the Last Name :" )

Name = Fname+" " +Lname
print ("Reverse Order :" + Name[::-1])
 

#Latha - First code - Assignment 1 - Problem 4
#4. Write a Python program to find the volume of a sphere with diameter 12 cm.
#Formula: V=4/3 * π * r

diameter=12
volume=(4/3)*(22/7)*(diameter/2)
volume = round(volume, 2)
print("Volume : " + str(volume))

 

