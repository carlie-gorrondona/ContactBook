# This is one of the excellent python projects for beginners. 
# Everyone uses a contact book to save contact details, including name, address, phone number, and even email address. 
# The main objective of this project is to generate a contact book using python where users can add a new contact, edit, or delete existing contacts and view the details 
# of all their contacts. This is one of the coolest project ideas in python for beginners to help strengthen their command of the programming language.
# You will need to use SQL to store the contacts. 


#--------------------- EXTERNAL LIBRARIES ---------------------#


#--------------------- FUNCTIONS & CLASSES ---------------------#

class Contact:
    def __init__(self, firstName, lastName, phoneNumber, email, address):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.email = email
        self.address = address

    def __str__(self):
        return f'\n First Name: {self.firstName}\n Last Name: {self.lastName}\n Phone Number: {self.phoneNumber}\n Email: {self.email}\n Address: {self.address}\n'
    
    # def get_firstName(self) -> str:
    #     return self.firstName
        
def mainMenu():
    print("* * * * * * * * * CONTACTS * * * * * * * * *")
    print("*           1. Create New Contact          *")
    print("*            2. Search Contacts            *")
    print("*             3. Edit Contact              *")
    print("*            4. Delete Contact             *")
    print("*                 5. Exit                  *")
    print("* * * * * * * * * * * * * * * * * * * * * * \n")

    userOption = input("Select an option: ")

    match userOption:
        case "1":
            createNewContact()
        case "2":
            searchContact()
        case "3":
            editContact()
        case "4":
            deleteContact()
        case "5":
            print("Goodbye")
        case _:
            print("Invalid entry")

def createNewContact():
    print("* * * * * * * * * CREATE NEW CONTACT * * * * * * * * *\n")

    inputFirstName = input("First Name: ")
    inputLastName = input("Last Name: ")
    inputPhoneNumber = input("Phone Number: ")
    inputEmail = input("Email: ")
    inputAddress = input("Address: ")

    newContact = Contact(inputFirstName, inputLastName, inputPhoneNumber, inputEmail, inputAddress)

    contactsArray.append(newContact)

    for contact in contactsArray:
        print(contact)
        
    print("Contact saved!")

    mainMenu()


def searchContact():
    print("Please enter the first name of the contact you would like to view.")
    userSearchInput = input("First Name: ")

    loopCount = 1

    for contact in contactsArray:
        if userSearchInput == contact.firstName:
            print(contact)
            searchContactMenu(contact)
        elif userSearchInput != contact.firstName and loopCount == len(contactsArray):
            print("Contact Not Found")
    
    

def searchContactMenu(contact):
    print("What would you like to do?")

    print("1. Edit Contact")
    print("2. Delete Contact")
    print("3. Search for Another Contact")
    print("4. Back to Main Menu")
    print("5. Exit")

    userOptionInput = input("Your selection: ")

    match userOptionInput:
        case "1":
            editContact(contact)
        case "2":
            deleteContact(contact)
        case "3":
            searchContact()
        case "4":
            mainMenu()
        case "5":
            print("Goodbye")
        case _:
            print("Invalid input")


def editContact(contact):
    print()

        
    

def deleteContact(contact):

    print("Are you sure you want to delete this contact?")
    userInputYorN = input("Enter 'Y' for 'Yes' or 'N' for 'No': ")

    match userInputYorN:
        case "Y":
            contactsArray.remove(contact)
            print("Contact deleted")
            for contact in contactsArray:
                print(contact)               
            mainMenu()
        case "N":
            searchContactMenu()
        case _:
            print("Invalid input")


#--------------------- MAIN ---------------------#

contactOne = Contact("Bubbles", "Smith", "123-123-0666", "bubbles@mailinator.com", "Shed")
contactTwo = Contact("Ricky", "Wells", "123-122-0000", "rwells@sunnyvale.com", "1 Bonneview")
contactThree = Contact("Julian", "Tremblay", "123-100-0000", "jtremblay@mailinator.com", "5 Maple Lake Drive")

contactsArray = [contactOne, contactTwo, contactThree]

mainMenu()