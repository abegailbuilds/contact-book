#The application should allow users to:
#Add contacts.
#View contacts.
#Search contacts.
#Update contacts.
#Delete contacts.
#Store and retrieve contact information.
#The project should use Git branches for at least one new feature.



contacts={}
choice=0

def addContact():
    contactId=input("Enter contact Id: ")
    name=input("Full name: ")
    age=input("Age: ")
    phoneNo=input("Phone number: ")
    email=input("Email address: ")
    homeaddress=input("Home Address: ")


    if contactId not in contacts.keys():
        contacts[contactId]={}

        contacts[contactId]["name"]=name
        contacts[contactId]["age"]=age
        contacts[contactId]["phoneNo"]=phoneNo
        contacts[contactId]["email"]=email
        contacts[contactId]["homeaddress"]=homeaddress

        print("Contact successfully added!")
    else:

        print("Contact already exists!")



def viewContact():

    for key,value in contacts.items():
        print(f"{key}:{value}")


def searchContact():

    contToSearch=input("Enter the contact Id to search: ")

    if contToSearch not in contacts.keys():
        print("Contact not found!")
        return

    else:
        print(f"Contact found: {contacts.get(contToSearch)}")


def updateContact():

    contToSearch=input("Enter contact Id to update: ")

    if contToSearch not in contacts.keys():
        print("Contact does not exist!")
        return

    else:
        newName = input("Enter new name or leave blank: ")
        newAge = input("Enter new age or ignore: ")
        newphoneNo = input("Enter new phone or ignore: ")
        newemail = input("Enter new email address or ignore: ")
        newaddress = input("Enter new home address or ignore: ")



    if len(newName) <= 0:
        pass

    else:
        contacts[contToSearch]["name"]=newName


    if len(newAge) <= 0:
        pass
    else:
        contacts[contToSearch]["age"]=newAge

    if len(newphoneNo) <= 0:
        pass
    else:
        contacts[contToSearch]["phoneNo"]=newphoneNo

    if len(newemail) > 0:
        contacts[contToSearch]["email"]=newemail
    else:
        pass

    if len(newaddress) > 0:
        contacts[contToSearch]["homeaddress"]=newaddress
    else:
        pass


    print("Contact successfully updated!")



def delContact():

    contToSearch=input("Enter contact Id to delete: ")

    if contToSearch not in contacts.keys():
        print("Contact not found!")

    else:

        contacts.pop(contToSearch)
        print(f"Contact deleted!")






def main():
    global choice

    while choice != 6:
        print("1. Add contacts")
        print("2. View contacts")
        print("3. Search contacts")
        print("4. Update contacts")
        print("5. Delete contacts")
        print("6. Exit")

        try:
            choice=int(input("Enter an option 1-6: "))

        except ValueError as e:
            print("Use numbers only")

        match choice:
            case 1:
              addContact()

            case 2:
                viewContact()

            case 3:
                searchContact()

            case 4:
                updateContact()

            case 5:
                delContact()

            case 6:

                break



if __name__=="__main__":
    main()