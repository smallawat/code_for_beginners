print("bill split app")
x=int(input("Enter the number of people"))
a = []
for i in range(x):
  print( "Enter the person name who paid")
  a.append(input())
  print("Enter the amount")
  a.append(input())
print(a)
def calsum(l):
    return sum([int(i) for i in l if type(i)==int or i.isdigit()])

total=(print("the total amount is",calsum(a)))
tot=int(calsum(a))

mean= (tot/x)
print("the equal split amount is",mean)
  
for i in range (x):
    price = mean - (type(i)==int)
    print(price)
if price > 0:
        print("owns ",price)
        
else:
         print("get money",price)#
         
         ##