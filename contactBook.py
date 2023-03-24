# This is one of the excellent python projects for beginners. 
# Everyone uses a contact book to save contact details, including name, address, phone number, and even email address. 
# The main objective of this project is to generate a contact book using python where users can add a new contact, edit, or delete existing contacts and view the details 
# of all their contacts. This is one of the coolest project ideas in python for beginners to help strengthen their command of the programming language.
# You will need to use SQL to store the contacts. 


#--------------------- EXTERNAL LIBRARIES ---------------------#


#--------------------- FUNCTIONS & CLASSES ---------------------#

class ContactBook:
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
            editContactFromMainMenu()
        case "4":
            deleteContactFromMainMenu()
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

    newContact = ContactBook(inputFirstName, inputLastName, inputPhoneNumber, inputEmail, inputAddress)

    contactsArray.append(newContact)

    for contact in contactsArray:
        print(contact)
        
    print("Contact saved!")

    mainMenu()


def searchContact():
    print("Please enter the first name of the contact you would like to view.")
    userSearchInput = input("First Name: ")

    loopCount = 1
    notFound = True

    for contact in contactsArray:
        if userSearchInput == contact.firstName:
            print(contact)
            searchContactMenu(contact)
            notFound = False
        
    if notFound:
        print("Contact Not Found")
        mainMenu()
            
    

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

def editContactFromMainMenu():
    print("Please enter the first name of the contact you would like to edit.")
    userSearchToEditInput = input("First Name: ")

    loopCount = 1
    notFound = True

    for contact in contactsArray:
        if userSearchToEditInput == contact.firstName:
            print(contact)
            editContact(contact)
            notFound = False
    if notFound:
        print("Contact Not Found")
        mainMenu()

def editContact(contact):
    print("What would you like to edit?")
    print("1. First Name")
    print("2. Last Name")
    print("3. Phone Number")
    print("4. Email")
    print("5. Address")
    print("6. All Fields")
    print("7. Back to Main Menu")
    userEditInput = input("Your Selection: ")

    match userEditInput:
        case "1":
            print("Enter contact's first name.")
            userFirstNameInput = input("First Name: ")
            contact.firstName = userFirstNameInput
            print("Contact updated")
            editAnotherFieldMenu()
        case "2":
            print("Enter contact's last name.")
            userLastNameInput = input("Last Name: ")
            contact.lastName = userLastNameInput
            print("Contact updated")
            editAnotherFieldMenu()
        case "3":
            print("Enter contact's phone number.")
            userPhoneNumberInput = input("Phone Number: ")
            contact.phoneNumber = userPhoneNumberInput
            print("Contact updated")
            editAnotherFieldMenu()
        case "4":
            print("Enter contact's email.")
            userEmailInput = input("Email: ")
            contact.email = userEmailInput
            print("Contact updated")
            editAnotherFieldMenu()
        case "5":
            print("Enter contact's address.")
            userAddressInput = input("Address: ")
            contact.address = userAddressInput
            print("Contact updated")
            editAnotherFieldMenu()
        case "6":
            print("Enter contact's first name.")
            userFirstNameInput = input("First Name: ")
            contact.firstName = userFirstNameInput
            print("Enter contact's last name.")
            userLastNameInput = input("Last Name: ")
            contact.lastName = userLastNameInput
            print("Enter contact's phone number.")
            userPhoneNumberInput = input("Phone Number: ")
            contact.phoneNumber = userPhoneNumberInput
            print("Enter contact's email.")
            userEmailInput = input("Email: ")
            contact.email = userEmailInput
            print("Enter contact's address.")
            userAddressInput = input("Address: ")
            contact.address = userAddressInput
            print("Contact updated")
            mainMenu()
        case "7":
            mainMenu()
        case _:
            print("Invalid input")

def editAnotherFieldMenu():
    print("Would you like to edit something else?")
    userEditInput = input("Enter 'Y' for 'Yes' or 'N' for 'No': ")

    match userEditInput:
        case 'Y':
            editContact()
        case 'N':
            mainMenu()

def deleteContactFromMainMenu():
    print("Please enter the first name of the contact you would like to view.")
    userSearchToDeleteInput = input("First Name: ")

    loopCount = 1
    notFound = True

    for contact in contactsArray:
        if userSearchToDeleteInput == contact.firstName:
            print(contact)
            deleteContact(contact)
            notFound = False

    if notFound:
        print("Contact Not Found")
        mainMenu()

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

contactOne = ContactBook("Bubbles", "Smith", "123-123-0666", "bubbles@mailinator.com", "Shed")
contactTwo = ContactBook("Ricky", "Wells", "123-122-0000", "rwells@sunnyvale.com", "1 Bonneview")
contactThree = ContactBook("Julian", "Tremblay", "123-100-0000", "jtremblay@mailinator.com", "5 Maple Lake Drive")

contactsArray = [contactOne, contactTwo, contactThree]

mainMenu()