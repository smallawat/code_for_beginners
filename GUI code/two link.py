print("bill split app")
x=int(input("Enter the number of people"))
a = []
b = []
for i in range(x):
  print( "Enter the person name who paid")
  a.append(input())
  print("Enter the amount")
  b.append(input())
print(a)
print(b)
print("the total amount is: ",sum(b))
mean=(total/x)
print("the equal split amount is",mean)
for i in range (x):
    price = mean - b[i]
    print(price)
if price > 0:
        print(a[i],"owns ",price)
        
else:
        print(a[i],"get money",price)
         