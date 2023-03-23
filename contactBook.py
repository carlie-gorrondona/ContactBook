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
        return f'\n First Name: {self.firstName}\n Last Name: {self.lastName}\n Phone Number: {self.phoneNumber}\n Email: {self.email}\n Addres: {self.address}\n'
        

def createNewContact():
    print("* * * * * * * * * CREATE NEW CONTACT * * * * * * * * *\n")

    inputFirstName = input("First Name: ")
    inputLastName = input("Last Name: ")
    inputPhoneNumber = input("Phone Number: ")
    inputEmail = input("Email: ")
    inputAddress = input("Address: ")

    firstContact = Contact(inputFirstName, inputLastName, inputPhoneNumber, inputEmail, inputAddress)

    print(str(firstContact))


# def searchContact():

# def editContact():

# def deleteContact():


#--------------------- MAIN ---------------------#

print("* * * * * * * * * CONTACTS * * * * * * * * *")
print("*           1. Create New Contact          *")
print("*             2. Search Contacts           *")
print("*             3. Edit Contact              *")
print("*             4. Delete Contact            *")
print("*                  5. Exit                 *")
print("* * * * * * * * * * * * * * * * * * * * * * \n")

userOption = input("Select an option: ")

match userOption:
    case "1":
        createNewContact()
    case "2":
        searchContacts()
    case "3":
        editContact()
    case "4":
        deleteContact()
    case "5":
        print("Goodbye")
    case _:
        print("Invalid entry")