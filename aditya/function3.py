#given int values, return True if one is '-ve' and one is +ve
#exept if the parameter negativeis true then return true ponly if both is _ve
#pos_neg(1,-1,false) true
def pos_neg(a,b):
    return a,b
parameter=input("enter true or false:")
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
if a<0 and b<0 and parameter=="true":
    print("true")
elif a>0 and b<0 and parameter=="false":
    print("true")
elif a<0 and b>0 and parameter=="false":
    print("true")
else:
    print("false")

   