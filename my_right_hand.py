import os

######################################################################## Class creation ##########################################################################

class Menu:
    
    def __init__(self, option_1, option_2, option_3, option_4, method_1, method_2, method_3, method_4):
        '''Allows for the creation of main menus and sub-menus'''
        
        self.option_1 = option_1
        self.option_2 = option_2
        self.option_3 = option_3
        self.option_4 = option_4
        
        
        self.method_1 = method_1
        self.method_2 = method_2
        self.method_3 = method_3   
        self.method_4 = method_4  

    def show_menu(self):
        '''Displays the menu to the users, with options numbers corresponding 
           to matching method numbers.'''  
        
        while True:                        
        # presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
          print()
          menu = input(f'''Select one of the following Options below:          
                {self.option_1[0].lower()} - {self.option_1} 
                {self.option_2[0].lower()} - {self.option_2} 
                {self.option_3[0].lower()} - {self.option_3}           
                {self.option_4[0].lower()} - {self.option_4}         
        :       ''').lower()              

          if menu == self.option_1[0].lower():
            self.method_1()                

          elif menu == self.option_2[0].lower():
            self.method_2()                                  
              
          elif menu == self.option_3[0].lower():
            self.method_3()
                                                  
          elif menu == self.option_4[0].lower():
            self.method_4()                
                
          else:
            print("\n!! Choose a valid option. !!\n")            
  
class Phonebook:            
    '''Creates a phonebook in which contacts can be added, edited, viewed, 
       or searched for.'''
    def __init__(self, txt_file, main_menu, sub_menu_1, sub_menu_2):
        
        # Text file to save to
        self.txt_file = txt_file
        
        # Menus to display to navigate methods.
        self.main_menu = main_menu
        self.sub_menu_1 = sub_menu_1
        self.sub_menu_2 = sub_menu_2
        
        # List of dictionaries in which to save contacts.       
        self.contact_list = []
        
        # Instance variables needed to access current contact searched for.
        self.current_contact = ""                
        self.new_name = ""
        self.new_number = 0
        self.current_index = 0
        self.search_name = ""

        # Flags.
        self.search_success = False
        self.adding_new_contact = False
        self.name_checked = False
        self.details_checked = False
        self.editing_name_only = False        
        self.editing_number_only = False
        self.editing_both = False
        self.discrete_searching = False
        self.search_already_done = False
        
        # Create the .txt file if it doesn't exist 
        if not os.path.exists(txt_file):
            with open(txt_file, "w") as default_file:
                pass
        
        # Make sure self.contact_list contains latest contact details that are
        # saved in the .txt file.
        self.update_contact_list(txt_file)                   


    def view_contacts(self):
        '''Displays the contacts in alphabetical order.'''        
        
        # Reset flags if arriving here after a search.
        if self.search_already_done:
            self.reset_flags_and_variables()
        
        self.update_contact_list(self.txt_file)
                
        sorted_contact_list = self.bubble_sort(self.contact_list) # Sort contact list alphabetically by name.                

        if sorted_contact_list == []:
            print("\n!! Your contacts list is empty !!\n") 
        else:            
            for contact in sorted_contact_list:                                        
                print(f"\nname: {contact['name']}\n")
                print(f"number: {contact['number']}\n\n")
                print("------------------------\n")                                  
            
            self.sub_menu_1()
    

    def bubble_sort(self, contact_list):
        '''Sorts the contact list alphabetically by name.'''
        swapped = False

        n = len(contact_list)

        for i in range(n):

            # Nested loop to iterate through each dictionary, indexed as 'j'
            for j in range(0, n-i-1):

                # Variables for name values in dictionaries next to each other in contact_list.
                name1 = contact_list[j]["name"]
                name2 = contact_list[j+1]["name"]

                # Swap contact order if name value closer to 'a' in alphabet.
                if name1 > name2:

                    contact_list[j], contact_list[j+1] = contact_list[j+1], contact_list[j]
                    swapped = True

            # Exit outer loop and stop comparing if single swap not made (i.e. list already in order).
            if not swapped:
                break

        return contact_list    
    
    
    def binary_search(self, name, contact_list, start=0, end=None):
        '''searches for inputted name by dividing contact_list in half each time.'''

        if end is None:
            end = len(contact_list) - 1

        if start <= end:            
            halfway = (start + end) // 2 # Use integer division to avoid error with index due to float.              
            
            # Ensure rest of program - e.g. delete() and embedded_delete() - can access the contact found within self.current_contact and self.current_index variable.
            if contact_list[halfway]["name"].lower() == name.lower():
                self.current_contact = contact_list[halfway] 
                self.current_index = self.contact_list.index(self.current_contact) 
                self.search_success = True

            elif contact_list[halfway]["name"].lower() > name.lower():
                
                return self.binary_search(name, contact_list, start, halfway - 1) # Search in the left half of the contact_list.  
            else:
                
                return self.binary_search(name, contact_list, halfway + 1, end) # Search in the right half of the contact_list.
        else:
            
            return # Return if not found, leaving self.search_success as False
    
    def search(self):
        '''Searches for a contact (by name) when 'search' is discretely selected 
           and then displays name and number.'''                                                      
        
        # If directed here from 'search again' option, flags need to be reset.
        if self.search_already_done:
            self.reset_flags_and_variables()

        self.discrete_searching = True                
        
        self.update_contact_list(self.txt_file)  
        
        if self.contact_list == []:
            print("\n!! Your contacts list is empty !!\n")
            self.main_menu()
            
        else:                        
            self.binary_search(input("\nEnter contact name to search for: "), self.bubble_sort(self.contact_list))                                               
                                                                                                                                                  
        if self.search_success == False: 
            print(f"\n!! This contact has not yet been added !!\n")
                            
            self.main_menu() # Return to main menu to allow user to search again.                        
            
        else:
            self.display_success_of_search_or_change_or_addition()
                            
            self.search_success = False # Reset flag.
            
            # Keep track of when a search has already been done so that different logic is applied
            # after calling methods from next sub-menu e.g. delete *this* contact.
            self.search_already_done = True
                                                       
            self.sub_menu_2()              
    
    def delete_contact(self):
        '''Deletes contact details for given name.'''
        
        # Reset flags if arriving here after a search.
        if self.search_already_done:
            self.reset_flags_and_variables()
        
        name = input("\nType the name of the contact that you would like to delete: ")                  

        self.binary_search(name, self.bubble_sort(self.contact_list)) # Search to find out if name exists and assign the dictionary to self.current_contact if it does.
        
        if self.search_success == False:
            
            print("\n!! This contact has not yet been added !!\n")
            
            self.main_menu            

        else:
            
            self.contact_list.remove(self.current_contact)                                 
        
            print("\n\n** Contact deleted **\n\n")        
                                    
            self.write_to_txt_file(self.txt_file) 
            
        self.reset_flags_and_variables()
        
        self.main_menu

    def insert_new_contact(self, name, number):
        '''Inserts a new contact into the self.contact_list list of dictionaries.'''
        
        new_contact = {"name": name, "number": number}                
        self.contact_list.append(new_contact)
        
        return

    def add_contact(self):
        '''Adds new contact to the self.contact_list instance variable 
           or saves edited contacts to said list.'''                                

        # Find out if user is adding a new contact (as opposed to editing) and perform checks for valid data
        # input if so.         
        if self.editing_name_only == False and self.editing_number_only == False and self.editing_both == False and self.details_checked == False:
            
            self.adding_new_contact = True                        
                        
            self.check_name_is_valid() # This check will prompt for a name, check its validity then lead onto prompting for a number before checking number validity.      
               
        elif self.adding_new_contact:
                                                           
            self.insert_new_contact(self.new_name, self.new_number) # Add new_name and new_number as a dictionary if adding a new contact (i.e. if not in editing mode).                                    
            
        self.display_success_of_search_or_change_or_addition()
        
        self.write_to_txt_file(self.txt_file)                
                
        self.reset_flags_and_variables()       
                
        self.main_menu()
    

    def check_name_is_valid(self):
        '''Checks that the name inputted is valid (used in add_contact, 
           edit_name and edit_number).'''
        
        while True:                            
            
            # Let user know they are entering a 'new' name if editing or adding new contact.
            if self.adding_new_contact or self.editing_name_only or self.editing_both:
                self.new_name = (input("\nEnter new contact name: "))
            else:
                self.new_name = (input("\nEnter contact name: "))
            
            
            if self.new_name.isnumeric() or self.name_is_a_float(self.new_name):
                                
                print("\n!! You need to enter a name, not a number !!\n")
            
            elif self.new_name.lower() == "back":
                print("\n!! This is a menu option so can't be used as a name - that's just confusing !!\n")
                
            
            elif len(self.new_name) > 20:
                print("\n!! You have entered too many characters. Try again !!")
                
            elif self.new_name == "" or self.new_name == " ":
                ("\n!! You did not enter a name. Try again !!")
                                            
            else:                
                
                self.binary_search(self.new_name, self.bubble_sort(self.contact_list)) # Search to check if contact already exists.
                        
                if self.search_success:
                    print("\n!! This contact already exists. Pick a different name !!\n")            
                                
                    self.search_success = False # Reset search_success flag so as not to disrupt logic further into program.
                
                # Call edit_number method to return to edit rest of edit_number process if 
                # check_number_is_valid was called at the start of edit_number method.
                else:                    
                    self.name_checked = True                        
                    self.edit_name()                
                    

    def name_is_a_float(self, name):
        '''Checks if the inputted name is a float, as part of 
           check_name_is_valid() method.'''
        try: 
            float(name)
            return True
        
        except ValueError:
            return False


    def check_number_is_valid(self):
        '''Checks that the number inputted is valid (used in 
           add_contact, edit_name and edit_number).'''                

        while True:                        
            try:
                self.new_number = int(input("Enter new contact number: "))                
                
                digit_list = [int(x) for x in str(self.new_number)] # Change number inputted to list of digits so their length can be counted.
                                
                if len(digit_list) > 11:
                    print("\n!! You have entered too many digits. Try again !!")                                
                
                # Call edit_number method to return to edit rest of edit_number process if 
                # check_number_is_valid was called at the start of edit_number method.
                else:
                    self.details_checked = True                    
                    self.edit_number()                                                
                                         
            except ValueError:
                print("\n!! You need to enter a number !!\n")
                

    def edit_choices(self):
        '''Directs user to correct edit method.'''
        
        while True:
            # Prompt user to input name to edit if they haven't selected 'edit this contact' from
            # the search sub-menu.
            if self.search_already_done == False:
                
                self.search_name = input('''\nType the name of the contact that you would like to edit or type 'back' to go back: ''')            
                        
                self.binary_search(self.search_name, self.bubble_sort(self.contact_list)) # Find inputted name from self.contact_list and save contact to self.current_contact.
                
            if self.search_already_done == False and self.search_success == False:
                print(f"\n!! This contact has not yet been added !!\n")
                self.sub_menu_1()
            
            elif self.search_name.lower() == "back":
                                
                self.search_success = False                
                main_menu.show_menu()
        
            else:
                option = input("Type 'na' to edit 'name', 'nu' to edit 'number', or 'b' to edit both: ").lower()
                
                self.search_success = False
                
                if option == "b":
                    self.editing_both = True                    
                    self.edit_name() # edit_name() logic will lead user to edit_number() if 'both' selected.
                elif option == "na":
                    self.editing_name_only = True     
                    self.edit_name()
                elif option == "nu":
                    self.editing_number_only = True
                    self.edit_number()
                else:
                    print("!! Choose a valid option !!")
                            
                
    def edit_name(self):
        '''Allows the user to edit a name.'''                                           
        
        # Check that the new name inputted is valid.
        if self.name_checked == False:
            self.check_name_is_valid()        
        
        elif self.adding_new_contact == False:                        
            self.contact_list[self.current_index]["name"] = self.new_name # Change the contact in contact_list if name check has been passed.                                                                
            
        # Make sure self.new_number has a value so thet display_contact has a 
        # valid variable to display after add_contact called.
        if self.editing_name_only:            
            self.new_number = self.contact_list[self.current_index]["number"]
            self.add_contact()                                                                             
        
        else:                        
                        
            self.binary_search(self.new_name, self.bubble_sort(self.contact_list)) # Make sure current_contact is known when editing both name & number.
                        
            self.edit_number() # Return to edit number if 'edit both' or 'add contact' option chosen.


    def edit_number(self):        
        '''Allows the user to edit a number.'''
        
        # Check that the new number inputted is valid.
        if self.details_checked == False:                        
            self.check_number_is_valid()                
        
        # Change the contact in contact_list if number check has been passed
        # and user is editing the number.
        elif self.adding_new_contact == False:            
            self.contact_list[self.current_index]["number"] = self.new_number            

        # Make sure self.new_name has a value so thet display_contact has a 
        # valid variable to display after add_contact called.
        if self.editing_number_only:
            self.new_name = self.contact_list[self.current_index]["name"]            
            self.add_contact()                        
            
        else:            
            
            self.add_contact() # Details are now saved within add_contact()                        
        
                               
    def delete_current_contact(self):
        '''Deletes the current contact when selected from the discrete search sub-menu.'''
        
        self.contact_list.remove(self.current_contact)
                        
        print("\n\n** Contact deleted **\n\n")
        
        self.write_to_txt_file(self.txt_file)                
        
        self.reset_flags_and_variables()
        
        self.main_menu()
        

    def reset_flags_and_variables(self):
        '''Resests flags and variables after contacts added'''
    
        # Reset flags.
        self.details_checked = False
        self.name_checked = False
        self.adding_new_contact = False                
        self.search_success = False
        self.editing_name_only = False        
        self.editing_number_only = False 
        self.editing_both = False
        self.discrete_searching = False
        self.search_already_done = False

        # Reset instance variables.
        self.new_number = 0
        self.current_index = 0
        self.current_contact = ""                
        self.new_name = ""        
        self.search_name = ""       


    def display_success_of_search_or_change_or_addition(self):
        '''Displays a confirmation of searched-for, added or edited contact.'''
        
        if self.discrete_searching and self.search_already_done == False:
            print("\n** Contact found **\n")
            print(f"name: {self.contact_list[self.current_index]['name']}\n")
            print(f"number: {self.contact_list[self.current_index]['number']}\n")            
        else: 
            print("\n** Contact saved **\n")
            print(f"name: {self.new_name}\n")
            print(f"number: {self.new_number}\n")                                                   
    
        
    def write_to_txt_file(self, txt_file):
        '''Writes changes made to the contacts in self.contact_list to a .txt file.'''
        
        # Change each dictionary in self.contact_list to a sublist of string pairs so that it can be written to .text file.
        with open(txt_file, "w") as contacts_file:
            contact_list_to_write = []
            for c in self.contact_list:
                str_attributes = [
                    c['name'],
                    str(c['number'])                    
                ]
                contact_list_to_write.append(";".join(str_attributes))
            contacts_file.write("\n".join(contact_list_to_write))

    def update_contact_list(self, txt_file):
        '''Saves the updated .txt file to contact_list.'''
        
        with open(txt_file, "r+") as current_contacts:
                        
            self.contact_data = current_contacts.read().split("\n") # Read the contents and move them into a list, separated where there is a newline character.
            self.contact_data = [c for c in self.contact_data if c != ""] # Reformat list so that it doesn't contain blank spaces.
            
            self.contact_list = [] # Clear self.contact_list of old data.
            
            for contact_str in self.contact_data:
                curr_contacts = {}
                                
                contact_components = contact_str.split(";")                 
                curr_contacts['name'] = contact_components[0]
                curr_contacts['number'] = contact_components[1]                
                                                                  
                self.contact_list.append(curr_contacts)                    


############################################# Instantiating objects ###########################################################################################

my_phonebook = Phonebook("contacts.txt", None, None, None) # Instantiate the phonebook class with placeholders for the menus that are yet to be instantiated.                

# Instantiate the main menu and sub-menus.
main_menu = Menu("Add a contact", "View contacts", "Search for a contact", "Exit", my_phonebook.add_contact, my_phonebook.view_contacts, 
                 my_phonebook.search, exit)

view_menu = Menu("Add a contact", "Edit a contact", "Delete a contact", "Home", my_phonebook.add_contact, my_phonebook.edit_choices, 
                my_phonebook.delete_contact, main_menu.show_menu)

search_menu = Menu("Delete this contact", "Edit this contact", "Search again", "Home", my_phonebook.delete_current_contact, my_phonebook.edit_choices, 
                my_phonebook.search, main_menu.show_menu)


# Update the menus in my_phonebook object now that they have been instantiated.
my_phonebook.main_menu = main_menu.show_menu
my_phonebook.sub_menu_1 = view_menu.show_menu
my_phonebook.sub_menu_2 = search_menu.show_menu

########################################### Initialising the program #########################################################################################

main_menu.show_menu() # Display the main menu as the first page of the program.
