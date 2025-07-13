from manager import load_contact_file,display_menue,choice_handling

# main func 
def main(): 
    """
    Main func that runs the contact manager application

    initialize contact manager by loading existing contacts from csv file
    then enters main prpgram loop. Loop continues until the user makes a choice to exit
    displays menue and handles user choice. 
    Loads contacts from contacts csv 
    reuns until user selects exit option
    handles user interaction through menue system 

    Returns: 
        None: Func funs contact manager application

    """
    load_contact_file()
    choice = 0
    while choice != 6:
        choice = display_menue()
        choice_handling(choice) 
        
if __name__ == "__main__":
    main()