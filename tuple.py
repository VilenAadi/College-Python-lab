#wap to find the 4th from the first and last
# t_1=(800,'user',300,400,'csai',500,600,'btech')
# print("4th from thr first:",t_1[3])
# print("4th from the last:",t_1[-4])
# Defining the tuple
# my_tuple = (10, 20, 30, 40, 50)

# Finding the index of an element
# element = 30
# index = my_tuple.index(element)

# print(f"The index of {element} is {index}")
# my_tuple = (10, 20, 30, 40, 50)
# print(my_tuple)
# element=int(input("Enter the element whose index you want to find: "))
# if element in my_tuple:
#     index = my_tuple.index(element)
#     print(f"The index of {element} is {index}")
# else:
#     print(f"{element} is not present in the tuple")
#WAP to convert list into tuple
# my_list = (10, 20, 30, 40, 50)
# my_tuple=tuple(my_list)
# print(f"List: {my_list}")
# print(f"Tuple: {my_tuple}")
# WAP to replace last value with 100
t_1=(800,'user',300,400,'csai',500,600,'btech')
k=list(t_1)
k[-1]=100
print(k)
