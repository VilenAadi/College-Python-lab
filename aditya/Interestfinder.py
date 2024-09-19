gender=input("enter gender M/F: ")
age=int(input("enter age:"))
if (gender=="F" and 1<age<58):
    print("the percentage of interest is 8.2")
elif(gender=="F" and 58<age<100):
    print("teh percentage of interest id 9.2")
elif(gender=="M" and 1<age<58):
    print("percentage interest 8.4")
elif(gender=="M" and 58<age<100):
    print("percentage intereest is 9.4")    