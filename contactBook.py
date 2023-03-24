#--------------------- FUNCTIONS & CLASSES ---------------------#

# Class that stores contact info
class ContactBook:
    def __init__(self, firstName, lastName, phoneNumber, email, address):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.email = email
        self.address = address

    def __str__(self):
        return f'\n First Name: {self.firstName}\n Last Name: {self.lastName}\n Phone Number: {self.phoneNumber}\n Email: {self.email}\n Address: {self.address}\n'
    
# Function that prints the main menu, takes a user input to select which menu option they want, and calls a function for that specific menu option.      
def mainMenu():
    print("* * * * * * * * * CONTACTS MENU * * * * * * * * *")
    print("*             1. Create New Contact             *")
    print("*              2. Search Contacts               *")
    print("*                3. Edit Contact                *")
    print("*               4. Delete Contact               *")
    print("*                    5. Exit                    *")
    print("* * * * * * * * * * * * * * * * * * * * * * * * *")

    userOption = input("Select an option: ")
    print("\n")

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
            print("Invalid entry. Please try again.\n\n")
            mainMenu()

# This function is called from the main menu when the user wants to create a new contact. Once all required info is submitted by the user, and new contact is created
# for the ContactBook class and appended to the contactsArray. All contacts are printed afterwards so the user can view all of their contacts including the newly
# created one. The user is then brought back to the main menu with mainMenu().
def createNewContact():
    print("* * * * * * * * * CREATE NEW CONTACT * * * * * * * * *")

    inputFirstName = input("First Name: ")
    inputLastName = input("Last Name: ")
    inputPhoneNumber = input("Phone Number: ")
    inputEmail = input("Email: ")
    inputAddress = input("Address: ")

    newContact = ContactBook(inputFirstName, inputLastName, inputPhoneNumber, inputEmail, inputAddress)

    contactsArray.append(newContact)

    for contact in contactsArray:
        print(contact)
        
    print("Contact saved!\n\n")

    mainMenu()

# This function allows the user to search for a contact based on first name alone. If the contact is located, then it prints to the screen and the searchContactMenu()
# function runs to display options for the user to select. If the contact is not located then, "Contact not found" is printed and the user is brought back to the main
# menu.
def searchContact():
    print("* * * * * * * * * SEARCH CONTACTS LIST * * * * * * * * *")

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
            
# This function runs when after the user has successfully located a contact from search. They can now choose to edit, delete, search for another contact, go back to
# the main menu, or exit. For edit, delete, search and main menu, a function is called depending on which option the user selects. 
def searchContactMenu(contact):
    print("What would you like to do?")

    print("1. Edit Contact")
    print("2. Delete Contact")
    print("3. Search for Another Contact")
    print("4. Back to Main Menu")
    print("5. Exit")

    userOptionInput = input("Your selection: ")
    print("\n")

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

# This function runs if the user wants to locate a contact that they want to edit. The user is required to enter the first name of the contact. Once located, the contact
# prints to the terminal and the editContact() function is called so the user can make changes.
def editContactFromMainMenu():
    print("* * * * * * * * * EDIT CONTACT * * * * * * * * *")
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

# This function allows the user to edit any field or all fields of a contact. If the user just selects one field to edit, then once the edit is complete, 
# editAnotherFieldMenu() is called in case the user wants to edit a second field.
def editContact(contact):
    print("* * * * * * * * * EDIT CONTACT * * * * * * * * *")
    print("What would you like to edit?")
    print("1. First Name")
    print("2. Last Name")
    print("3. Phone Number")
    print("4. Email")
    print("5. Address")
    print("6. All Fields")
    print("7. Back to Main Menu")
    userEditInput = input("Your Selection: ")
    print("\n")

    match userEditInput:
        case "1":
            print("Enter contact's first name.")
            userFirstNameInput = input("First Name: ")
            contact.firstName = userFirstNameInput
            print("\n")
            print("Contact updated\n")
            editAnotherFieldMenu(contact)
        case "2":
            print("Enter contact's last name.")
            userLastNameInput = input("Last Name: ")
            contact.lastName = userLastNameInput
            print("\n")
            print("Contact updated\n")
            editAnotherFieldMenu(contact)
        case "3":
            print("Enter contact's phone number.")
            userPhoneNumberInput = input("Phone Number: ")
            contact.phoneNumber = userPhoneNumberInput
            print("\n")
            print("Contact updated\n")
            editAnotherFieldMenu(contact)
        case "4":
            print("Enter contact's email.")
            userEmailInput = input("Email: ")
            contact.email = userEmailInput
            print("\n")
            print("Contact updated\n")
            editAnotherFieldMenu(contact)
        case "5":
            print("Enter contact's address.")
            userAddressInput = input("Address: ")
            contact.address = userAddressInput
            print("\n")
            print("Contact updated\n")
            editAnotherFieldMenu(contact)
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
            print("\n")
            print("Contact updated")
            mainMenu()
        case "7":
            mainMenu()
        case _:
            print("Invalid input")

# This function allows the user to edit another field from the same contact they edited previously. If the user selects 'Y', then editContact() is called and they are
# brought back to the edit menu. If the user selects 'N', then they are brought back to the main menu.
def editAnotherFieldMenu(contact):
    print("Would you like to edit something else?")
    userEditInput = input("Enter 'Y' for 'Yes' or 'N' for 'No': ")
    print("\n")

    match userEditInput:
        case 'Y':
            editContact(contact)
        case 'N':
            mainMenu()

# This function allows the user to locate a contact that they want to delete. They are asked to enter the contact's first name.
# If found, the contact prints to the screen and the deleteContact() function is called. If not found, "Contact not found" prints and the user is brought back to 
# the main menu.
def deleteContactFromMainMenu():
    print("* * * * * * * * * DELETE CONTACT * * * * * * * * *")
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
        print("\n")
        mainMenu()

# THis function allows the user to delete a contact. They are first asked if they are sure they want to delete the contact. If they select 'Y', then the contact is deleted,
# the contacts list prints so the user can make sure it was deleted, and the user is brought back to the main menu. If the user selects 'N', then they are brought
# to the main menu.
def deleteContact(contact):
    print("* * * * * * * * * DELETE CONTACT * * * * * * * * *")
    print("Are you sure you want to delete this contact?")
    userInputYorN = input("Enter 'Y' for 'Yes' or 'N' for 'No': ")
    print("\n")

    match userInputYorN:
        case "Y":
            contactsArray.remove(contact)
            print("Contact deleted\n")
            for contact in contactsArray:
                print(contact)               
                mainMenu()
        case "N":
            mainMenu()
        case _:
            print("Invalid input")


#--------------------- MAIN ---------------------#

# premade contacts for ContactBook class
contactOne = ContactBook("Bubbles", "Smith", "123-123-0666", "bubbles@mailinator.com", "Shed")
contactTwo = ContactBook("Ricky", "Wells", "123-122-0000", "rwells@sunnyvale.com", "1 Bonneview")
contactThree = ContactBook("Julian", "Tremblay", "123-100-0000", "jtremblay@mailinator.com", "5 Maple Lake Drive")

# Array that stores the premade contacts
contactsArray = [contactOne, contactTwo, contactThree]

mainMenu()