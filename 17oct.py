# 17th Oct 2024
# ADITYA KUMAR CHAUHAN
# 2300971520016

##s1='wipro companies technology'
##print(s1,id(s1))
##s2=s1[1:5]
##print(s2)
##s1='wipro companies technology is {}'
##num=210011100
##print(s1.format(num))

# s1='My name is {} '
# s2='your roll no. is {}'
# name=input("Enter your name: ")
# num=int(input("Enter your roll no. :"))
# print(s1.format(name))
# print(s2.format(num))

# s1='Today is our day'
# print(s1.split(" "))

# s1='Today is our day'
# print(s1.split(" ")[0:2])

# first=input("Enter your first name: ")
# middle=input("Enter your middle name: ")
# last=input("Enter your last name: ")
# s1='My Name is {}{}{} '
# print(s1.format(first,middle,last))

list_a=[4,5,4,3,3,4,3,4,3,8,5,6,5,6,5,6,7,8,9,3,4]

count = {}
for element in list_a:
    if element in count:
        count[element] += 1
    else:
        count[element] = 1
for element, count in count.items():
    if count > 3:
        print(element)