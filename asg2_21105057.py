 #Assignment 2



#program 1
print('#program 1')
string= input("Enter the string =")
#a
length=len(string) 
print("A. Length of the entered string =",length)
#b
rev=string[::-1]
print("B. Revere of the string:",rev)
#c
new_string=string[slice(10,35,1)]
print("C. Sliced string :",new_string)
#d
str2=string.replace("a case sensitive","object oriented")
print("D.String after replacement:",str2)
#e
index=string.index("a")
print("E.Index of 'a' in the string =",index)
#f
string.replace(" ","")
print("F.String after removal of WHITESPACES :",string)
print("")
