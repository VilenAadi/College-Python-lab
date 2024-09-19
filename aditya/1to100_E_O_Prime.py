#write a program to print a no. is either even or odd ranging from 1 to 100
for num in range (1,101):
    if num%2==0:
       print("even no.",num)
    if num%2==1:
        print("odd no.",num)
    if num==2:
        print("prime no.",num)
        continue
    for i in range (2,num):
        if num%i==0:
            break
        elif i==num-1:
            print("prime no.",num)
            
        
            