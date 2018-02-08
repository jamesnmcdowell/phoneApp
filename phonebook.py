#Most recent version

import pickle

class Contact(object):
    def __init__(self, name, phone, email, website):
        self.name = name
        self.phone = phone
        self.email = email 
        self.website = website 

    def __repr__(self):
        return "{} {} {} {}".format(self.name, self.phone, self.email, self.website)
    
#     def modifyEntry(self):
        
class Phonebook(object):
    def __init__(self, phonebook):
        self.phonebook = phonebook
        self.list = []
        
    def __repr__(self):
        return "{}".format(self.phonebook)

    def lookupPerson(self, name):
        nameFound = False
        for entry in self.phonebook:  
            if name == entry.name:
                print("{} {} {} {} ".format(entry.name, entry.phone, entry.email, entry.website))
                nameFound = True

        if nameFound == False:
            print("The name you entered does not exist within the phonebook")  

    def addEntry(self, name, phone, email, website):
        contact = Contact(name, phone, email, website)
        self.phonebook.append(contact)
        print("You have successfully added the following entry: {} {} {} {}".format(name, phone, email, website))
     
    def deleteEntry(self, name):
        nameFound = False
        for entry in self.phonebook:  
            if name == entry.name:
                print("You deleted the following Entry: {}: {}".format(name, entry.phone))
                self.phonebook.remove(entry)
                print(self.phonebook)
                nameFound = True

        if nameFound == False:
            print("The name you entered does not exist within the phonebook") 
        
    def viewAll(self):
        for entry in self.phonebook:
            print("{} {} {} {} ".format(entry.name, entry.phone, entry.email, entry.website))
    
    def save(self):   
        # open the file in write mode (w)
        file = open('phonebook.pickle','wb')
        # dump the contents of the phonebook_dict into myfile - the open file
        print(self.phonebook)
        pickle.dump(self.phonebook, file)
        # close myfile
        file.close()    
    
    def load(self):
        # open the file in read mode (r)
        file = open('phonebook.pickle', 'rb')
        # load the contents from the file and store it in the phonebook_dict variable
        self.phonebook = pickle.load(file)

    def quit(self):
        print("You have quit the application")
       

running = True

james = Contact("james","770-256-4525", "james@gmail.com", "www.james.com")
sam = Contact("sam", "770-666-6666", "sam@gmail.com", "www.sam.com")
matt = Contact("matt","770-245-9996", "matt@gmail.com", "www.matt.com")   
rebecca = Contact("rebecca", "770-224-1115", "rebecca@gmail.com", "www.rebecca.com")
phonebook = Phonebook([james, sam, matt, rebecca] )
  
load = input("Would you like to load your contacts from a previous save?") 
if load == 'yes':
    phonebook.load()
    
print("Electronic Phone Book \n===================== ")
print("1. Look up an entry ")
print("2. Set an entry ")
print("3. Delete an entry\n4. List all entries \n5. Modify Entry\n5. Quit ")     
while running:
    choice = int(input("What do you want to do (1-6)?"))
    if choice == 1:
        name = input("Enter the person's name: ")
        phonebook.lookupPerson(name)
    elif choice == 2:
        name = input("Enter the person's name: ")
        phone = input("Enter the person's phone number: ")
        email = input("Enter the person's email: ")
        website = input("Enter the person's website: ")
        phonebook.addEntry(name, phone, email, website)
    elif choice == 3:
        name = input("Enter the person's name: ")
        phonebook.deleteEntry(name)
    elif choice == 4:
        phonebook.viewAll()
#     elif choice == 5:
#         modifyEntry(self)
    elif choice == 6:
        save = input("Would you like to save your entries?")
        if save == "yes":
            phonebook.save()
            print("You have successfully saved your file")
        phonebook.quit()
        running = False
    else:
        print("You have inputed an invalid response. Please try again.")
    