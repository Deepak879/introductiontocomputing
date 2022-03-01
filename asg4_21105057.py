               #Assignment 4






#program 1

print("#program 1")
#defining tower of Hanoi function
def tower_of_hanoi(n,fro,to,aux):
    if n==0:
        return

    tower_of_hanoi(n-1,fro,aux,to)
    print(f"Move disk {n} from {fro} to {to}")
    tower_of_hanoi(n-1,aux,to,fro)

#calling function for 3 disks
tower_of_hanoi(3,'A','C','B')
print("")




#program 2

print("#program 2")

#input rows
n= int(input("Enter the number of rows in Pascal's triangle:"))

#using recursions
print("Recursive Approach:")
def pascal(n,col=n):
    if n<0:
        return "ERROR!, Row can't be negative."
    if n == 0:
        return
    
    pascal(n-1,col)

    #printing the spaces
    print(' '*(col-n), end='')
    
    #first number  is always 1
    entry = 1
    for i in range(1,n+1):
        
        print(entry,end ='  ')

        #using Binomial Coefficient
        entry= entry*(n-i)//i
    print()
pascal(n)
print("")

#using iterations.
print("Iteractive Approach:")
for row in range(1,n+1):
    

      #printing spaces
      print(' '*(n-row),end='')       #for ith row (n-i)th spaceshas to be printed

      cell = 1
      #assigning values to cellon reaching the jth column
      for col in range(1,row+1):
           print(cell,end='  ')

           cell=cell*(row-col)//col
      print()
print("")




#program 3
print("#program 3")
print("Enter the value so as int_1 > int_2")
int_1=int(input("Enter integer 1 ="))
int_2=int(input("Enter integer 2 ="))
remainder=int_1%int_2                   #calculating remainder
quotient=int_1//int_2                   #calculaing quotient
print("Reemainder is =",remainder)
print("Quotient is =",quotient)
#checking remainder and quotient are non zero
if (remainder!=0):
    if (quotient!=0):
        print("Both values are non zero")
    else:
        print("quotient is non zero")
else:
    if (quotient!=0):
        print("remainder is zero")
    else:
        print("Both values are zero")
#adding data into set and updating values
set1=set()
for i in range(4,7):
    a=remainder+i
    b=quotient+i
    if (a>4):
        set1.add(a)
        print(set1)
    if (b>4):
        set1.add(b)
        print(set1)
    else:
        continue

print(set1)
set2=frozenset(set1)
print("Immutable set: ",frozenset(set1))
print("Max value in the set: ",max(set2))
print("Hash value: ",hash(max(set2)))
print("")




#program 4
print("#program 4")
#creating class
class student:
    #intialising the constructor
    def __init__(self,name,sid):
        self.name = name
        self.sid = sid
    #printing the data
    def stu_info(self):
        print("Student Name : ",self.name)
        print("SID : ",self.sid)
    #calling destructor
    def __del__(self):
        print("Destructor called,data deleted")

#creating object of class
student1 = student("Deepak Kalyan",21105057)

#calling instance method using object data
student1.stu_info()

#deleting the object
del student1

print("")





#program 5
print("#program 5")
#creating a class named Employee
class Employee:
    #intialising the contructor.
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __del__(self):
        print(f"Employee {self.name} record deleted")

#creating employee records
employee1 = Employee("Mehak",40000)
employee2 = Employee("Ashok",50000)
employee3 = Employee("Viren",60000)

#part a ,Updating salary
employee1.salary = 70000
print(f"(a)The updated salary of the employee {employee1.name} is {employee1.salary}")

#part b, deleting a record
print("(b) ",end='')
del employee3

print("")

  



#program 6
print("#program 6")
#George's word
word1 = input("Enter George's word =")
#Barbie's guessed word
word2 = input("Enter Barbie's guessed word =")

def count_in_dict(word1):
    count={}
    list1=list(word1.lower())

    n=len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] +=1
        else:
            count[list1[i]] =1
    return count

#test
if count_in_dict(word1)!= count_in_dict(word2):
    print("The letters aren't exist,hence friendship is fake!!")


#shopkeeper's input
def userinput():
    ans = input("\nDoes the word makes sense?(Y or N)")

    if ans == 'Y':
        print("The friend pass the test!!")
    elif ans == 'N':
        print("The word doesn't have a meaning, friendship is fake!!")
    else:
        print("Invalid input,try again")
        print("")
        



