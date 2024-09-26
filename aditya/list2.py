lst=[]
n=int(input("enter the number of elements: "))
for i in range(0,n):
    lst1=int (input())
    lst.append(lst1)
print(lst)
lst.sort()
print(lst)
lst.reverse()
print(lst)
print("longest element",lst[3])