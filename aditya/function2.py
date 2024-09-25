#we have a loud talking parrot.The hour parameter is current hour time in the range 0......23.
# we are in trouble if the parrot is talking and the hour is before7 or after 20.
# return true if we are in trouble
def parrot_trouble(p,b):
    return p,b
p=input("enter yes if your parrot is talking and no if not:")
b=int(input("enter the hour of taking:")) 
if  p=="yes" and b<7 or b>20 :
    print("trouble")
else:
    print("no trouble") 
