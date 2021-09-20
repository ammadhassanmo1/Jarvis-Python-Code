total = 0
while(True):
    
    menu1 = '''  Welcome to Gondal General Store
            1. Press 'q' to Quit    
            2. press 'a' to add more items    '''
    print(menu1)
    choice = input("Enter Your Choice\n")
    if choice == 'q':
        break
    elif choice == 'a':
        sum = int(input("Enter the price\n"))
        total = total+sum
        print(f"Your Bill So far is {total} ")

    else:
        print("Enter Right Choice")


print(f"Your total bill is {total}")
