dict = ()
while True:
    print("birthdate collelation app")
    print("1.show the birthday")
    print("2.add birthday to the list")
    print("3.Exit")
    choice = int(input("Enter the chocie"))
    if choice ==1:
        if len(dict.keys()) ==0:
            print("nothing to show")
        else:
            name=input("Enter name")
            birthday=dict.get(name,"No data found")
            print(birthday)
    elif chocie ==2:
        name=input("Enter the name")
        date=input("Enter the date")
        dict[name]=date
        print("Birthday added")
    elif chocie ==3:
        break
    else:
        print("chose a valid option")
    