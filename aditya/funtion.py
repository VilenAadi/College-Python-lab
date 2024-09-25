#given two int values return their sum  when the 2 values are same then return double their sum
def sum_double(a,b):
    return a+b
a=int(input("Enter a:"))
b=int(input("Enter b:"))
if a!=b:
    sum=sum_double(a,b)
    print("sum is",sum)
else:
    sum=2*sum_double(a,b)
    print("sum is",sum)
