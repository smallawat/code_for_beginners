print("This is splitwise app")
x=int(input("Enter the number of people"))
my_list=[]
for i in range(x):
    print("enter the name of person")
    my_list.append(input())
print(my_list)
y=int(input("enter the amount"))
z=input("Enter the name of peson who paid")
c=int(y/x)
print("the disturbion is",c)
a=int(y-c)
# print("the amount expect given one",a)
b=int(a/(x-1))
print("the splitetd amount is",b,"given to",z)




    

