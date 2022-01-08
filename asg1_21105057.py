   #Assignment 1

                   



              #1st program 
print(" 1st program ")
#python program  to find the average of the three numbers
print("python program  to find the average of the three numbers")
num_1=int(input("enter the first number ="))
num_2=int(input("enter the second number ="))
num_3=int(input("enter the third number ="))

sum=num_1+num_2+num_3
avg=sum/3
print("the average of the numbers entered =",avg)
print("")


   
              #2nd program
print(" 2nd program ")
#program to find the person's income tax
print('/n',"all tax payers are charged a flat tax rate of 20%",'/n',"all tax payers are allowed a $10000 standard deduction",'/n',"for each dependent, a taxpayer is allowed a deduction of $3000")

gross_income = float(input("enter the gross income to standard penny ="))
std_ded=10000
dep=int(input("enter the number of dependents="))
dep_ded=3000
taxable_income=gross_income-std_ded-(dep_ded*dep)
print("taxable income =$",taxable_income)
tax=(taxable_income*20)/100
print("he tax to be paid by the person is= $",tax)
print("")



              #3rd pogram
print(" #3rd program ")
#program to store diffrent data values into a list.
print(" python program to store diffrent data values into a list")

SID = int(input("enter the SID ="))
Name = input("enter the name =")
Gender = input("enter the gender F/M =")
Course = input("enter the course name =")
CGPA = float(input("enter the CGPA ="))
student=['SID','Name','Gender','Course','CGPA']
print(student)
print("")



            #4TH program
print(" 4th program ")
#program to enter the marks of five students
print("program to enter the marks of five students")
m1=float(input("enter the marks of 1st student="))
m2=float(input("enter the marks of 2nd student="))
m3=float(input("enter the marks of 3rd student="))
m4=float(input("enter the marks of 4th student="))
m5=float(input("enter the marks of 5th student="))
marks=[m1,m2,m3,m4,m5]
marks.sort()
print(marks)
print("")



            #5th program
print(" #5th program ")
list_color =['Red','Green','White','Black','Pink','Yellow']

#5.a)program to print a specified list after removing 4th element
print("program to print a specified list after removing 4th element")
color=['Red','Green','White','Black','Pink','Yellow']
color.remove('Black')
print(color)

#5.b)program to print a specified list after removing 'Black' and 'Pink' from the list and replace it with 'Purple'
print("program to print a specified list after removing 'Black' and 'Pink' from the list and replace it with 'Purple'")
color=['Red','Green','White','Black','Pink','Yellow']
color[3:5]=["Purple"]
print(color)
print("")




