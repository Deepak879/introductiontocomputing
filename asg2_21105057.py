    #Assignment 2



    #program 1

print('#program 1')
string= input("Enter the string : ")
#a
length=len(string) 
print("A. Length of the entered string : ",length)
#b
rev=string[::-1]
print("B. Revere of the string: ",rev)
#c
new_string=string[slice(10,35,1)]
print("C. Sliced string : ",new_string)
#d
str2=string.replace("a case sensitive","object oriented")
print("D.String after replacement : ",str2)
#e
index=string.index("a")
print("E.Index of 'a' in the string : ",index)
#f
str3=string.replace(" ","")
print("F.removal of blank whitespaces with empty string : ",str3)
print("")



    #program 2
print(' #program 2')
Name= "DEEPAK KALYAN"
SID= 21105057
Department_Name= "ECE"
CGPA= 9.9
intro= "Hey, \n {} Here!.\nMy SID is {} \nI am from {} Department and My CGPA is {}"
print(intro.format(Name,SID,Department_Name,CGPA))
print("")



    #program 3
print(' #program 3')
a=56
b=10
print("a. a&b=  ",(a&b))
print("b. a|b=  ",(a|b))
print("c. a^b=  ",(a^b))
print("d. Left shift both a and b with 2 bits :",(a << 2,b <<2))
print("e. Right shift a with 2 bits and b with 4 bits: ",(a >> 2,b >> 4))
print("")



    #program 4
print(' #program 4')
num1= int(input("Enter first number :"))
num2= int(input("Enter second number :"))
num3= int(input("Enter third number :"))
if num1 > num2:
  if num1 > num3:
      highest_number = num1
  else:
      highest_number = num3

if num2 > num1:
  if num2 > num3:
    highest_number = num2
  else:
    highest_number = num3
print("highest_number = ",num1 or num2 or num3)
print("")


     #program 5
print(' #program 5')
input_string = input("Enter input string: ")
if "name" in input_string:
    print("Yes")
else:
    print("No")
print("")



     #program 6
print(' #program 6')
side1= float(input("Length of first side = "))
side2= float(input("Length of second side = "))
side3= float(input("Length of third side = "))
if side1 > side2+side3 or side2 > side3+side1 or side3 > side1+side2:
   print("No,Triangle can't be made.")
else:
   print("Yes,Trangle can be made.")
print("")
