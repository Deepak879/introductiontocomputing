        #Assignment 1





#program 1
print("#program 1")
#taking input from user
sentence= input("Enter the string =").lower().split()
i=0
#defining empty dictionary to use later to store element,counter pairs and eliminating common letters and words 
dict={}

#checking if the string input is a word or a sentence
if " " not in sentence:
 #searching for common letters
 while i<len(sentence):
    counter=0
    k=0
    while k<len(sentence):
       if sentence[i]==sentence[k]:
          counter=counter+1
          k=k+1
       else:
          k=k+1
    #storing values in dictionary
    dict[f"{sentence[i]}"]= counter
    i=i+1
else:
 #making list of words using split method
 list=str.split(sentence)
 #searching for common words
 while i<len(list):
   counter=0
   k=0
   while k<len(list):
         if list[i]==list[k]:
             counter=counter+1
             k=k+1
         else:
              k=k+1
              #storing the pairs in dictionary
              dict[f"{list[i]}"]=counter
              i=i+1
#printing the final result
print("Total occurences")
for key,value in dict.items():
    print(f"{key}-{value}")
    print("")






#program 2
print("#program 2")
#taking input from  user
day=int(input("Enter day="))
month=int(input("Enter month="))
year=int(input("Enter year="))

#Removing all the invalid cases
if day>30 and month in {2,4,6,9,11}:
    condition=False
elif day>31 and month in {1,3,5,7,8,10,12}:
    condition=False
elif (day==29 or day==30) and month==2 and year%4!=0:
    condition=False
elif day==30 and month==2 and year%4==0:
    condition=False
else:
    condition=True

#After checking the condition, following if-else statementis executed
if condition:
    #checking and changing for new year
    if day==31 and month==12:
       n_year=year+1
    else:
        n_year=year
    if month==12 and day==31:
        n_month=1
    else:
        n_month=month
#changing dates
    #checking for months with 31 days
    if month in {1,3,5,7,10,12}:
        if day==31:
           next_day=1
           if month!=12:
               n_month=month+1
           else:
               n_month=1
        else:
            next_day=day+1
    #checking for the month of february
    elif month==2:
       if year%4==0:
           if day==29:
               next_day=1
               n_month=3
           else:
               next_day=day+1
       else:
           if day==28:
              next_day=1
           else:
               next_day=day+1
               n_month=3
    #covering all the remaining cases
    else:  
        if day==30:
           next_day=1
           n_month=month+1
        else:
           next_day=day+1
   #printing the calculations
    print(f"Next Date is:{next_day}/{n_month}/{n_year}")
    print("")






#program 3
print("#program 3")
#taking input list
list1=eval(input("Enter the list: "))
list2=[]
for n in list1:
    list2.append((n,n**2))
print("Output:",list2)
print("")









#program 4
print("#program 4")
grade_point=int(input("Enter grade points="))
dic={10:"Your grade is 'A+' and Outstanding performance.",
     9:"Your grade is 'A' and Excellent performance.",
     8:"Your grade is 'B+' and Very Good performance.",
     7:"Your grade is 'B' and Good performance.",
     6:"Your grade is 'C+' and Average performance.",
     5:"Your grade is 'C' and Below Average performance.",
     4:"Your grade is 'D' and Poor performance."}
if 4<=grade_point<=10:
    statement=dic.get(grade_point)
    print(statement)
else:
    print("'Error!'")
    print("")








#program 5
print("#program 5")
print("the  pattern is given below :")
letr= "ABCDEFGHIJK"
j=0
while len(letr)-j*2 >=1:
      print(" "*j + letr[0 : len(letr)-j*2])
      j+=1
      print("")








#program 6
print("#program 6")
#by default
repeat="YES"
#Intiallly empty dictionary
dic1={}
dic2={}
#list containing Y or N
list=["YES","Y","NO","N"]
while repeat=="YES" or repeat=="Y":
    #taking input
    name = input("Enter student name =")
    sid = int(input("Enter student's SID ="))
    if sid<0:
        print("Error! SID can't be negative")
    else:
        #updating dic1 with 'sid': 'name'
        dic1.update({sid:name})
        #updating dic2 with 'name': 'sid'(will be helpful while sorting)
        dic2.update({name:sid})
        #asking if want to enter more input or not
        repeat = input("Enter YES/Y to continue or NO/N to end =")
    if repeat=="NO" or repeat=="N":
        break
    elif(not(repeat in list)):
        print("Error! please inter valid input['YES' or 'N']")
        repeat = input("Enter'YES' to continue and 'NO' to end =")

print("Q6.(a)")
print("The dictionary containing {'SID':'Name'} is shown below")
print(dic1)

print("Q6.(b)")
list_k=sorted(dic2)
dic3={}
for i in list_k:
    dic3.update({dic2.get(i):i})
print("The dictionary after sorting according to name =")
print(dic3)

print("Q6.(c)")
sort_dic1=sorted(dic1)
dic4={}
for i in sort_dic1:
    dic4.update({i:dic1.get(i)})
print("The dictionary after sorting according to SID =")
print(dic4)

print("Q6.((d)")
enter_sid= int(input("Enter SID to get name of student ="))
#searching for sid as key in dic1
output_name= str(dic1.get(enter_sid))
#printing name with key sid
print("Name of student with above SID is =",{output_name})
print("")





#program 7
print("#program 7")
#Taking input
n=int(input("Enter number of elements N in fibonacci series: [N must be positive Integer]: N="))
#printing error message when N<=0
if n<=0 :
    print("Error! Number of elements in fibonacci series must be integer and greater than zero.")
#code for fibonacci series
else:
    #code for fibonacci series for first 2 elements
    if n == 1:
        print("The fibonacci series with 1 element is shown below ,[1]")
        print("Average of given fibonacci series is", 1)
    elif n == 2:
        print("The fibonacci series with 2 element is shown below,[1,1]")
        print("Average of given fibonacci series is", 1)
    #General code for fibonacci for next N-2 elements
    else:
        # List of fibonacci elements with 1,1 as initial elements
        list1 = [1, 1]
        #Building logic to get fibonacci series
        a = 1
        b = 1
        # For loop
        for i in range(n - 2):
            s = a + b
            list1.append(s)
            a = b
            b = s
        # printing the final fibonacci series
        print("The fibonacci series with {n} elements is shown below:")
        print(list1)
        # Finding average of fibonacci series
        sum = 0    #intial sum=0
        # finding sum of all elements in list1
        for num in list1:
            sum = sum + num
        average = (sum / n)
        # Till two decimal place
        two_decimal = "{:.2f}".format(average)
        # printing average
        print("Average of given fibonacci series is =",{two_decimal})
        print("")






#program 8
print("#program 8")
set1= {1,2,3,4,5}
set2= {2,4,6,8}
set3= {1,5,9,13,17}

print("Q8.(a)")
print("(a).Set of all elements that are in Set1 and Set2 but not both =")
set4=set1^set2
print(set4)

print("Q8.(b)")
print("(b).Set of all elements that are in only one of the three sets Set1,Set2 and Set3 =")
set5= set1^set2^set3
print(set5)

print("Q8.(c)")
print("(c).Set of elements that are exactly two of the sets Set1,Set2 and Set3 =")
set6= (set1|set2|set3) - (set1^set2^set3) - (set1&set2&set3)
print(set6)

print("Q8.(d)")
print("(d).Set of all integers in the range 1 to 10 that are not in Set1 =")
set7=set()
for i in range(1,11):
    if i not in set1:
        set7.add(i)
print(set7)

print("Q8.(e)")
print("(e).Set of all integers in the range 1 to 10 that are not in Set1,Set2 and Set3 =")
set8=set(range(1,11)) - (set1|set2|set3)
print(set8)
print("")
