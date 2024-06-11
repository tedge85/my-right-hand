## BUGS ##
# Add contact is allowing duplicates. /
# Search not finding existing contacts. /
# edit does not find existing contacts. /
# Add delete options underneath delete method - edit this contact, delete this contact, home /
# Main menu not appearing after delete_this_contact action. / 
# Edit_this_contact doesn't work. /
# Delete a contact doesn't work. /
# Make Phonebook class self-contained - menus as parameters. /
# In edit options: option 'b' changed to 'back' to avoid not being able to edit. /
# 'Back' can no longer be added to contacts or edited in. /
# Search option needs to be bypassed if search success == False. /
# Refactored code so more modular.





# 'back' no longer works when navigating edit menu.

# Incorporate e_search back into search? Carefullt!!!!








# GET RID OF DEV PRINTING FOR TESTS
# Cut unuseful comments

import os

######################################################################## Class creation ##########################################################################

class Menu:
    
    def __init__(self, option_1, option_2, option_3, option_4, method_1, method_2, method_3, method_4):
        
        # Options to pick from menu.
        self.option_1 = option_1
        self.option_2 = option_2
        self.option_3 = option_3
        self.option_4 = option_4
        
        # Methods to call.
        self.method_1 = method_1
        self.method_2 = method_2
        self.method_3 = method_3   
        self.method_4 = method_4  

    def show_menu(self):
        '''Displays the menu.'''  
        
        while True:                        
        # presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
          print()
          menu = input(f'''Select one of the following Options below:          
                {self.option_1[0].lower()} - {self.option_1} 
                {self.option_2[0].lower()} - {self.option_2} 
                {self.option_3[0].lower()} - {self.option_3}           
                {self.option_4[0].lower()} - {self.option_4}         
        : ''').lower()              

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
    
    def __init__(self, txt_file, main_menu, sub_menu_1, sub_menu_2):
        
        # Text file to save to
        self.txt_file = txt_file
        
        # Menus to display to navigate methods.
        self.main_menu = main_menu
        self.sub_menu_1 = sub_menu_1
        self.sub_menu_2 = sub_menu_2
        
        # List of dictionaries in which to save contacts.       
        self.contact_list = []
        
        # Instance variable needed to access current contact searched for.
        self.current_contact = ""                
        self.new_name = ""
        self.new_number = 1
        self.current_index = 1

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
    
    def check_name_is_valid(self):
        '''Checks that the name inputted is valid (used in add_contact, edit_name and edit_number).'''
        
        while True:                            
            
            # Let user know they are entering a 'new' name if editing or adding new contact.
            if self.adding_new_contact or self.editing_name_only or self.editing_both:
                self.new_name = (input("\nEnter new contact name: "))
            else:
                self.new_name = (input("\nEnter contact name: "))
            
            # Check if name entered is a non-string.
            if self.new_name.isnumeric():
                
                # Error message if number added instead of name.
                print("\n!! You need to enter a name, not a number !!\n")                            
                
            # Error message if number is too long.
            elif len(self.new_name) > 20:
                print("\n!! You have entered too many characters. Try again !!")
                
            else:
                # Make sure self.contact_list is updated#############################################
                #self.update_contact_list("contacts.txt")############################################

                # Search to check if contact already exists.
                self.embedded_search(self.new_name)
        
                # Issue error message if contact does exist.
                if self.search_success:
                    print("\n!! This contact already exists. Pick a different name !!\n")            
            
                    # Reset search_success flag.
                    self.search_success = False
                
                # Call edit_number method to return to edit rest of edit_number process if 
                # check_number_is_valid was called at the start of edit_number method.
                else:                    
                    self.name_checked = True                        
                    self.edit_name()                
                    
    
    def check_number_is_valid(self):
        '''Checks that the number inputted is valid (used in add_contact, edit_name and edit_number).'''                

        while True:                        
            try:
                self.new_number = int(input("Enter new contact number: "))                

                # Change number inputted to list of digits so they can be counted.
                digit_list = [int(x) for x in str(self.new_number)]
                
                # Error message if number is too long.
                if len(digit_list) > 11:
                    print("\n!! You have entered too many digits. Try again !!")                                
                
                # Call edit_number method to return to edit rest of edit_number process if 
                # check_number_is_valid was called at the start of edit_number method.
                else:
                    self.details_checked = True
                    self.edit_number()                                                
            
            # Error capture if non-integer entered.                 
            except ValueError:
                print("\n!! You need to enter a number !!\n")
                

    def add_contact(self):
        '''Adds new contact to the contact_list instance variable.'''
                            
        # Find out if user is editing.
        if self.editing_name_only == False and self.editing_number_only == False and self.editing_both == False:
            self.adding_new_contact = True
        
        # Check input values if this hasn't been done yet (this then links to check_number_is_valid).        
        if self.name_checked == False and self.details_checked == False:                        
            self.check_name_is_valid()      
               
        # Add contact and number as a dictionary if new contact (not in editing mode).   
        if self.adding_new_contact:            
                
            # Add a new dictionary with the new details then add to contact_list.
            new_contact = {"name": self.new_name, "number": self.new_number}                
            self.contact_list.append(new_contact)                                
            
            # Use embedded search to get the current_index of newly added name, ready
            # to use in display_contact().
            self.embedded_search(self.new_name)
            
        self.display_contact()
        
        # Write the updated contact list to .txt file.        
        self.write_to_txt_file("contacts.txt")
        
        # Make sure self.contact_list matches .txt file. 
        self.update_contact_list("contacts.txt")
                
        self.reset_flags_and_variables()       
        
        # Return to main menu.
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

        # Reset instance variable.
        self.current_contact = ""                
        self.new_name = ""
        self.current_index = 1
        self.new_number = 1       

    def display_contact(self):
        '''Displays a confirmation of an edited or added contact.'''
        
        if self.discrete_searching == True and self.search_already_done == False:
            print("\n** Contact found **\n")
            print(f"name: {self.contact_list[self.current_index]['name']}\n")
            print(f"number: {self.contact_list[self.current_index]['number']}\n")            
        else: 
            print("\n** Contact saved **\n")
            print(f"name: {self.new_name}\n")
            print(f"number: {self.new_number}\n")  
            print(self.current_index) ###################################################
        
    def view_contacts(self):
        '''Displays the contacts in alphabetical order.'''        
        
        # Reset flags if arriving here after a search.
        if self.search_already_done == True:
            self.reset_flags_and_variables()

        # Update contact_list with latest contacts from saved .txt file.
        self.update_contact_list("contacts.txt")
        
        # Sort contact list alphabetically by name.
        sorted_contact_list = sorted(self.contact_list, key=lambda d: d['name'])
        
        # Check if contact list is empty and issue message if it is.
        if sorted_contact_list == []:
            print("\n!! Your contacts list is empty !!\n") 
        else:
            # If not empty, display contacts.
            for contact in sorted_contact_list:                                        
                print(f"\nname: {contact['name']}\n")
                print(f"number: {contact['number']}\n\n")
                print("------------------------\n")                                  
            
            self.sub_menu_1()
    
    def embedded_search(self, name):
        '''Searches for a contact (by name) to check if it exists.'''
        
        # iterate through list of dictionaries to see if inputted name
        # matches a contact name.
       
        for dict in self.contact_list:
            print(dict["name"].lower()) ################################################################
            if dict["name"].lower() == name.lower():
                self.search_success = True
            
                # Keep track of found contact to use in edit method.
                self.current_contact = dict
                self.current_index = self.contact_list.index(self.current_contact)                                
                print(f"are you here: {self.current_index}") #########################################################
                
        
        else:
            print("not found") #################################################################################
            self.search_success = False            
        
        return    
    
    def search(self):
        '''Searches for a contact (by name) and then displays name and number.'''                                                      

        # If directed here from 'seaerch gain' option, reset flags.
        if self.search_already_done == True:
            self.reset_flags_and_variables()

        self.discrete_searching = True                

        # Update contact_list with latest contacts from saved .txt file.
        self.update_contact_list("contacts.txt")  

        # Error message if contact list is empty.
        if self.contact_list == []:
            print("\n!! Your contacts list is empty !!\n")
            self.main_menu()
            
        else:            
            name = input("\nEnter contact name to search for: ")
            #self.embedded_search(input("\nEnter contact name to search for: "))          
            for dict in self.contact_list:                                        
                if dict["name"].lower() == name.lower():
                    self.search_success = True
            
                    # Keep track of found contact to use in edit method.
                    self.current_contact = dict
                    self.current_index = self.contact_list.index(self.current_contact)                
           
                                                                                                                                                  
        # Display message if searched name does not match a stored name.                        
        if self.search_success == False: 
            print("\n!! This contact has not yet been added !!\n")
                
            # Return to main menu to allow user to search again.
            self.main_menu()                        
            
        else:
            self.display_contact()
                
            # Reset flag.
            self.search_success = False 
            
            self.search_already_done = True

            # Display sub-menu option.                                           
            self.sub_menu_2()                       
    
    def edit_choices(self):
        '''Directs user to correct edit method.'''
        
        while True:
            # Prompt user to input name to edit if they haven't selected 'edit this contact'.
            if self.search_already_done == False:
                
                search_name = input("\nType the name of the contact that you would like to edit or type 'back' to go back: ")            
        
                # Find inputted name and save to self.current_contact
                self.embedded_search(search_name)
            
                # Reset flag.
                self.search_success = False
            
            if self.new_name.lower() == "back":
                main_menu.show_menu()
        
            else:
                option = input("Type 'na' to edit 'name', 'nu' to edit 'number', or 'b' to edit both: " ).lower()
            
                # Edit name and number if chosen:
                if option == "b":
                    self.editing_both = True
                    self.edit_name()
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
        print(self.name_checked) ####################################
        # Check that the new name inputted is valid.
        if self.name_checked == False:
            self.check_name_is_valid()        
        
        elif self.adding_new_contact == False:
            # Change the contact in contact_list if name check has been passed.            
            self.contact_list[self.current_index]["name"] = self.new_name                                                                
            
        # Make sure self.new_number has a value so thet display_contact has a 
        # valid variable to display after add_contact called.
        if self.editing_name_only:            
            self.new_number = self.contact_list[self.current_index]["number"]
            self.add_contact()                                                                             
        
        else:                        
            
            # Make sure current_contact is known when editing both name & number.
            self.embedded_search(self.new_name)
            
            # Return to edit number if 'edit both' or 'add contact' option chosen.
            self.edit_number()

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
        
            self.add_contact()                        
        
                               
    def delete_current_contact(self):
        '''Deletes the current contact when selected from search sub-menu.'''
        self.contact_list.remove(self.current_contact)
        
        # Display confirmation message.        
        print("\n\n** Contact deleted **\n\n")
        
        # Write the updated contact list to .txt file.        
        self.write_to_txt_file("contacts.txt")
        
        # Make sure self.contact_list matches .txt file. 
        self.update_contact_list("contacts.txt")
        
        self.reset_flags_and_variables()

        # Return to Home menu.
        self.main_menu()
        

    def delete_contact(self):
        '''Deletes contact details for given name.'''
        
        # Reset flags if arriving here after a search.
        if self.search_already_done == True:
            self.reset_flags_and_variables()
        
        name = input("\nType the name of the contact that you would like to delete: ")                  

        self.embedded_search(name)
        
        if self.search_success == False:
            
            print("\n! This contact has not been added yet !\n")
            

        else:
            
            self.contact_list.remove(self.current_contact)                                 
        
            # Display confirmation message.        
            print("\n\n** Contact deleted **\n\n")        
                
            # Write the updated contact list to .txt file.        
            self.write_to_txt_file("contacts.txt")
        
            # Make sure self.contact_list matches .txt file. 
            self.update_contact_list("contacts.txt")
        
        self.reset_flags_and_variables()
        
        self.main_menu
        
    def write_to_txt_file(self, txt_file):
        '''Writes changes made to the contacts in self.contact_list to a .txt file.'''
        
        with open(txt_file, "w") as contacts_file:
            contact_list_to_write = []
            for c in self.contact_list:
                str_attrs = [
                    c['name'],
                    str(c['number'])                    
                ]
                contact_list_to_write.append(";".join(str_attrs))
            contacts_file.write("\n".join(contact_list_to_write))

    def update_contact_list(self, txt_file):
        '''Saves the updated .txt file to the class variable contact_list.'''
        
        with open(txt_file, "r+") as current_contacts:
            
            self.contact_data = current_contacts.read().split("\n")
            self.contact_data = [c for c in self.contact_data if c != ""]

            # Clear self.contact_list of old data.
            self.contact_list = []
            
            for contact_str in self.contact_data:
                curr_contacts = {}
                
                # Split list components with semicolon and manually add each component to a dictionary for each contact.
                contact_components = contact_str.split(";")                 
                curr_contacts['name'] = contact_components[0]
                curr_contacts['number'] = contact_components[1]                

                # Save each contact in a list of dictionaries.                                                  
                self.contact_list.append(curr_contacts)                    


############################################# Instantiating objects ######################################################################################

# Instantiate the phonebook class with placeholders for the menus that are yet to be instantiated.                
my_phonebook = Phonebook("contacts.txt", None, None, None)

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

########################################### Starting the program #########################################################################################

# Display the main menu to show as the first page of the program.
main_menu.show_menu()
