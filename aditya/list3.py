lst=[]
n=int(input("enter the number of elements: "))
for i in range(0,n):
    lst1=int (input())
    lst.append(lst1)
print(lst)
lst.sort()
print(lst)
print("first largest element:",lst[0])
print(" second largest element:",lst[1])
print("third largest element:",lst[2])