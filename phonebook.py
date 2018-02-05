phonebook = {"James":"770-256-4525", "Steve":"770-355-6356", "John":"404-345-5677", "Albert":"678-345-4674"}


print("Electronic Phone Book \n===================== ")
print("1. Look up an entry ")
print("2. Set an entry")
print("3. Delete an entry\n4. List all entries \n5. Quit ")
running = True

while running:
    choice = int(input("What do you want to do (1-5)?"))
    if choice == 1:
        name = input("Enter the person's name: ").capitalize()
        if name in phonebook:
            print(phonebook[name])
        else:
            print ("This name does not exist within the phonebook")
    elif choice == 2:
        name = input("Enter the person's name: ").capitalize()
        phone = input("Enter the person's phone number: ")
        phonebook[name] = phone
        print("You have successfully added the following entry: {}:{}".format(name, phonebook[name]))
        print(phonebook)
    elif choice == 3:
        name = input("Enter the person's name: ").capitalize()
        if name in phonebook: 
            print("You deleted the following Entry: {}: {}".format(name,phonebook[name]))
            del phonebook[name]
            print(phonebook)
        else: 
            print("The name you entered does not exist within the phonebook")  
    elif choice == 4:
        for name in phonebook:
            print("Name: {} #{}".format(str(name).capitalize,phonebook[name]))
        print()
    elif choice == 5:
        print("You have quit the application")
        running = False
    else:
        print("You have inputed an invalid response. Please try again.")

