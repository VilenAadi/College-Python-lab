n=int(input("enter the number: "))
for num in range (1,n):
    for i in range (2,num):
        if num%i==0:
            break
        elif i==num-1:
            print("prime no.",num)