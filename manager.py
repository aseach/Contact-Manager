from contact import Contact
import sys
import csv
import re


# intializing contact dict
contact_dict = {} 
# Tuple menue options
MENU_OPTIONS = (
    "View all contacts",
    "Add a contact",
    "Edit a contact",
    "Delete a contact",
    "Search for a contact",
    "Exit"
)
# load csv file function
def load_contact_file (filename = 'contacts.csv'):
        """
        Loads Contacts from a CSV file into gloal dictionary(contact_dict)
        CSV has headers of: name, number, email,notes, birthday

        If CSV is empty or does not exist program will start with an empty dict

        Args: 
            Filename: path to CSV file wih stored contacts
        Load contacts from a CSV file into the global contact_dict.

        Returns: 
            None, modifies global dict 
      Raises:
            FileNotFoundError : handles file silently if not there 
        """
        try: 
            with open (filename, newline="") as file:
                    csvfile =csv.DictReader(file)
                    for line in csvfile:
                        name     = line['name']
                        number   = line['number']
                        email    = line['email']
                        notes    = line.get('notes', '')
                        birthday = line.get('birthday', '')
                        contact_dict[name] = Contact(name,number,email,notes,birthday)
        except FileNotFoundError:
                pass
# creating option menue
def display_menue ():
        """
        Prints main menue and prompts user to chose an option
        loops until user enters a valid integer between 1 and the num of menue options in tuple

        Returns:
            Int: the user's menue choice as an in (1-6)
        """
        print("Welcome to your contact manager!\n" )
        print ("Please choose an option: \n")
        for i , options in enumerate(MENU_OPTIONS , 1):
              print (f"{i} {options}")
        print()
        while True:
            user_input = input("Enter your choice (1-6): \n")
            if user_input.isdigit() and int(user_input) in range(1,7):
                    return int(user_input)
            else:
                    print ("Please choose an option of 1-6!")
# calling function depending on user input
def choice_handling (user_input):
        """
        Dispatches user's menu choice to the appropriate function

        Args:
            user_input = integer choice made from display_menue()
      Returns: 
            None: func calls other func according to arg
        """
        if user_input == 1:
                view_contacts()
        elif user_input == 2:
                add_contact()
        elif user_input == 3:
                edit_contact()
        elif user_input == 4:
                delete_contact()
        elif user_input == 5:
                search_contact()
        elif user_input == 6:
                exit_program()
#view all contacts func
def view_contacts():
    """
    Displays all saved contacts stored in contact_dict

    If no contacts in , displays the message telling user there are no contacts
    If there are contacts, will print each contacts info w/ separate line for easy reading

    Returns:
      None: func prints contact info into console using __str__ method format
    """
    print("")
    print ("==View All Contacts==\n")
    if not contact_dict:
           print ("There are no saved contacts right now!")
           return
    for name, info in contact_dict.items():
           print ("_" * 40)
           print("")
           print (info)          
# adding a contact function               
def add_contact():
        """
        asks user to enter information for a new contact then adds it to the dict
        collects name, number,email,notes, and birthday from user
        if contact with same name exists asks for confirmation
        saves updated contact list to csv file after new addition is successful

        Returns:
            None: func edits global contact_dict and saves to file 

      Note: 
            Able to handle multiple names by asking for confirmation
            auto saves cotnacts to csv after adding
            tells users notes and bithday are optional
        """
        print("==Add a New Contact==\n")
        name  = input("First and lastname of the person you want to add: ").strip()
        if name in contact_dict:
               while True:
                      continue_choice = input (" This name is already in your contacts, would you like to continue? (y/n) ").strip().lower()
                      if continue_choice == "y":
                            print(f"Adding new contact with name '{name}'...")
                            break
                      elif continue_choice == "n":
                             print ("Stopping contact adding!")
                             return
                      else : 
                             print ("please enter y or n ! ")
        number = input (" Enter the phone number: ").strip()
        email = input("Enter the email: ").strip()
        notes = input("Enter any notes (optional): ").strip()
        birthday = input("Enter the person's birthday (optional format: MM/DD/YYYY): ").strip()
        c = Contact(name,number,email,notes,birthday)
        contact_dict[name] = c 
        save_contacts_to_csv()
        print(f"\nContact '{name}' has been added successfully!")
# save contacts function
def save_contacts_to_csv (filename = 'contacts.csv'):
       """
       Saves al contacts from contact_dict to csv file 
       writes contact info to certain filepath with headers of
       name,number,email,notes,and birthday. Overwrites existing file 

       ARgs:
            filename(str): pathto csv where contacts are saved
                  defaulted to "contacts.csv
      Returns: 
            None: func writes data into csv file 
      Notes: 
            writes over entile file each save
            creates file if file does not exist
            yeses csv format w/ headers   
       Returns:
            None: Function writes data to file.
       """
       with open (filename, 'w', newline='') as csvfile:
              category_names = ['name','number','email','notes','birthday']
              writer = csv.DictWriter(csvfile, fieldnames = category_names)
              writer.writeheader()
              for contact in contact_dict.values():
                     writer.writerow({
                            'name' :contact.name,
                            'number' : contact.number,
                            'email' : contact.email,
                            'notes' : contact.notes,
                            'birthday' : contact.birthday
                            })
# edit contact funcation 
def edit_contact():
        """
        lets users to edit existing contact iinfo
        asks user to select who to edit via name
        provides options of diff fields to edit ( name, numer, email , etc.)
        updates contact dict and saves changes in csv file

        Returns:
            none: funcchanges contact_dict and saves to file 
      Note: 
            handles over name change by updating dic key 
            auto saves cotnacts to csv after editing
            gives feedback to user if contact does not exist
            input validation of menu choices (1-5)
        Allows the user to edit an existing contact's information.
        """
        print("==Editing a Contact==\n")
        edit_contact_input = input("First and Last name of the person you want to edit: \n").strip()
        if edit_contact_input in contact_dict:
            contact =contact_dict[edit_contact_input]
            print(f"Chosen_contact: {contact}" )
            print ("Please choose an option: \n")
            print("(1) change name\n")
            print("(2) change number\n")
            print("(3) change email\n")
            print("(4) change notes\n")
            print("(5) contact birthday\n")
            while True:
                edit_input = int(input("Enter your choice (1-5): \n"))
                if edit_input in [1,2,3,4,5]:
                      break
                else:
                        print ("Please choose an option of 1-5!")
            if edit_input == 1:
                new_name = input("new name: \n").strip()
                contact.name = new_name
                contact_dict[new_name] = contact
                del contact_dict[edit_contact_input]
                save_contacts_to_csv()
            elif edit_input == 2:
                new_number = input("new number: \n").strip()
                contact.number = new_number
                save_contacts_to_csv()
            elif edit_input == 3:
                new_email= input("new email: \n").strip()
                contact.email = new_email
                save_contacts_to_csv()
            elif edit_input == 4:
                new_notes = input("new notes: \n").strip()
                contact.notes = new_notes
                save_contacts_to_csv()
            elif edit_input == 5:
                new_birth= input("new birthday: \n").strip()
                contact.birthday = new_birth
                save_contacts_to_csv()
            print("\ncontact has been updated!")
        else:
              print("\nThis contact does not exist\n")
#delete a typed in contact
def delete_contact():
    """
    Deletes contact from contact dict
    asks user to enter name of contact they wish to delete.
    if cotnact exists func removes it from dict and saves updated dict to csv file

    Return: 
      None: func edits contact_dict and savesto csv file 

      Note: 
            give feed back if cotnact does nto exist 
            aut saces contacts to csv after contact is deleted
            uses exact name matching
    """
    print ("==Delete a Contact==\n")
    delete = input("First and Lastname of who you want to delete:  \n").strip()
    if delete in contact_dict:
        del contact_dict[delete]
        save_contacts_to_csv()
        print("The contact has been deleted! ")
    else:
        print ("That person is not in your contacts! \n")
def search_contact():
    """
    looks for contacts using various criteria then printing out the contact.
    four options:
      by name( case insensative)
      by number(exact matching)
      by email(case in sensative )
      by birthday month(partial matching)

     Uses regular expression fr pattern amtching 
     
     Returns: 
      None: func prints searched resuults to user in console

     Note:
      return first match found 
      uses case insensative matching for name and email
      give feed back if there are no matches 
      input validation for search type (1-4)
    """
    print("==Contact Search==\n")
    print("1. Search by name")
    print("2. Search by phone number")
    print("3. Search by email domain")
    print("4. Search by birthday month")
    while True:
        choice = input("Enter your choice (1-4): \n").strip()
        if not choice.isdigit():
            print ("Please choose an option of 1-4: ")
            continue
        if choice.isdigit() and range(1,5):
              choice = int(choice)
              break
    if choice == 1:
          name_chosen = input("First and Lastname of person you want to find: \n")
          pattern = re.compile(name_chosen , re.IGNORECASE)
          for name,contact in contact_dict.items():
                if pattern.search(contact.name):
                      print ("Contact found!\n")
                      print (contact)
                      return
                else:
                      print ("No contact under that name was found. Try again! ")
    if choice == 2:
          num_chosen = input("the number you want to find: \n")
          pattern = re.compile(num_chosen )
          for number,contact in contact_dict.items():
                if pattern.search(contact.number):
                      print ("Contact found!\n")
                      print (contact)
                      return
                else:
                      print ("No contact under that number was found. Try again! ")
    if choice == 3:
          email_chosen = input("the email of person you want to find: \n")
          pattern = re.compile(email_chosen , re.IGNORECASE)
          for email,contact in contact_dict.items():
                if pattern.search(contact.email):
                      print ("Contact found!\n")
                      print (contact)
                      return
                else:
                      print ("No contact under that email was found. Try again! ")
    if choice == 4:
          birth_chosen = input("the birthday of person you want to find(Format: MM/DD/YEAR): \n")
          pattern = re.compile(birth_chosen , re.IGNORECASE)
          for birth,contact in contact_dict.items():
                if pattern.search(contact.birthday):
                      print ("Contact found!\n")
                      print (contact)
                      return
                else:
                      print ("No contact under that name was found. Try again! ")
#exit program func
def exit_program():
        """
        Exit contact manager program
        Displays goodbye message and ends program using sys.exit()

        Returns: 
            None: function terminates program
        """
        print ("See you next time!")
        sys.exit()