
class Contact :
    """
    Class that represents a contact with persona inforamtion

    this class stores and manages individual contact information of name, number, email, 
    notes and birthday. It provides strong string rep to display the contact details

    Attributes:
        name(str): the contacts full name( first and last)
        number(str): the contacts phone number
        email (str): the contacts email address
        notes (str): optional notes about contact, empty default string
        birthday(str): optional birthday in MM/DD/YYY format, starts as empty default string.
    """
    def __init__(self, name , number, email,notes = '', birthday = ''):
        """
        Create a new contact with provided information. Notes and birthday are opt
         parameters that default to empty string

        Arguments:
            name(str): the contacts full name( first and last)
            number(str): the contacts phone number
            email (str): the contacts email address
            notes (str): optional notes about contact, empty default string
            birthday(str): optional birthday in MM/DD/YYY format, starts as empty default string.
        
        Returns:
            None: Constructor method.
        """
        self.name = name
        self.number = number
        self.email = email 
        self.notes = notes
        self.birthday = birthday
    def __str__(self):
        """
        Return formatted string representation of the contact

        provides human readable rep of contact info 
        shows each field on a separate line with clear albels

        Returns:
            Str: formated string wil cotnact information 
        """
        return (f"Name: {self.name}\n"
                f"Number: {self.number}\n"
                f"Email: {self.email}\n"
                f"Notes: {self.notes}\n"
                f"Birthday: {self.birthday}")
