## BUGS ##
# Add contact doesn't confirm contact added, just goes to view menu. /
# Add contact is allowing duplicates.
# Home command doesn't work on view menu /
# Search not finding existing contacts.
# edit does not find existing contacts.

import os

class Menu:
    
    def __init__(self, option_1, option_2, option_3, option_4, function_1, function_2, function_3, function_4):
        self.option_1 = option_1
        self.option_2 = option_2
        self.option_3 = option_3
        self.option_4 = option_4
        self.function_1 = function_1
        self.function_2 = function_2
        self.function_3 = function_3   
        self.function_4 = function_4  

    def show_menu(self):
        '''Displays main menu for user and task-related tasks.'''  
        
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
            self.function_1()                

          elif menu == self.option_2[0].lower():
            self.function_2()                                  
              
          elif menu == self.option_3[0].lower():
            self.function_3()
                                                  
          elif menu == self.option_4[0].lower():
            self.function_4()                
                
          else:
            print("\n!! Choose a valid option. !!\n")                                                                                                
  
class Phonebook:
    
    contact_list = []
    search_success = False
    embedded_delete = False
    
    def __init__(self, txt_file):
        self.txt_file = txt_file
           
        # Create the .txt file if it doesn't exist 
        if not os.path.exists(txt_file):
            with open(txt_file, "w") as default_file:
                pass
            
    def add_contact(self):
        '''adds new contact to the contact_list class variable'''
        
        while True:
            
            name = (input("\nEnter contact name: "))
                
            # Check if name entered is a non-string.
            if name.isnumeric():
                
                # Error message if number added instead of name.
                print("\n!! You need to enter a name, not a number !!\n")                            
                
            # Error message if number is too long.
            elif len(name) > 20:
                print("\n!! You have entered too many characters. Try again !!")
                
            else:
                # Make sure self.contact_list is updated
                self.update_contact_list("contacts.txt")

                # Search to check if contact already exists.
                self.embedded_search(name)
        
                # Issue error message if contact does exist.
                if self.search_success == True:
                    print("\n!! This contact already exists. Pick a different name !!\n")            
            
                    # Reset search_success flag.
                    self.search_success = False
                    
                else:
                    break
                
        while True:                        
            try:
                number = int(input("Enter contact number: "))
                
                # Use list comprehension so that number of digits can be counted.
                digit_list = [int(x) for x in str(number)]
                
                # Error message if number is too long.
                if len(digit_list) > 11:
                    print("\n!! You have entered too many digits. Try again !!")
                                        
                else:
                    
                    break
            
            # Error capture if non-integer entered.                 
            except ValueError:
                print("\n!! You need to enter a number !!\n")
            
                
        # Add contact and number as a dictionary if new contact.
        new_contact = {
            "name": name,
                "number": number
        }
            
        self.contact_list.append(new_contact)                
        
        # Write the updated contact list to .txt file.        
        self.write_to_txt_file("contacts.txt")
        
        # Make sure self.contact_list matches .txt file. 
        self.update_contact_list("contacts.txt")
        
        print("\n** Contact saved **\n")

        # Return to Home menu.
        main_menu.show_menu()
        
    def view_contacts(self):
        '''Displays the contacts in alphabetical order.'''        
        
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
            
            view_menu.show_menu()
    
    def embedded_search(self, name):
        '''Searches for a contact (by name) to check if it has already been added to contact_list.'''
        
        # Search contacts with name provided.
        # by iterating through list of dictionaries to match seached name to value.               
        for dict in self.contact_list:            
                for value in dict.values():                
                    if value.lower() == name.lower():
                        self.search_success = True
                    else:
                        self.search_success = False

    def search(self, name=("\nEnter contact name to search for: \n")):
        '''Searches for a contact (by name) and then displays name and number.'''                      
        
        name = input(name)
        
        # Update contact_list with latest contacts from saved .txt file.
        my_phonebook.update_contact_list("contacts.txt")  

        # Error message if contact list is empty.
        if my_phonebook.contact_list == []:
            print("\n!! Your contacts list is empty !!\n")
                    
        else:                               
            # Search contacts with name provided.
            # by iterating through list of dictionaries to match seached name to value.               
            for dict in self.contact_list:            
                for value in dict.values():                
                    if value.lower() == name.lower():
                        self.search_success = True
                        
                        # Display search result if sing discrete search method.
                        
                        print("\n------------------------\n")
                        print(f"\nname: {dict['name']}\n")
                        print(f"number: {dict['number']}\n")                    
                        print("\n------------------------\n")
                        break
                  
                # Display message if searched name matches a stored name (disable message 
                # if search carried out as part of another method).
                if my_phonebook.search_success == True:
                    print("\n** Contact found **\n")                  
                    
                    
                      
                # Display message if searched name does not match a stored name.
                else:
                    print("\n!! This contact has not yet been added !!\n")
                    
                # Reset flag
                my_phonebook.search_success = False
                      
                # Display sub-menu options.
                main_menu.show_menu()
                                            
    
    def edit_contact(self):
        '''Allows the user to edit a name or contact.'''         
        
        while True:
            name = input("\nType the name of the contact that you would like to edit or type 'b' to go back: ")
            
            # Going one menu back if 'b' chosen
            if name.lower() == "b":
                main_menu.show_menu()
            else:
                self.embedded_search(name)
                
                # Move to next edit prompt if name is found.
                if self.search_success == True:
                    break
                    
                    # Reset the successful search.
                    self.search_success = False                    
                    
                else:
                    print("\n!! That contact has not yet been added !!\n")
               
        while True:
            option = input("Type 'na' to edit 'name', 'nu' to edit 'number', or 'b' to edit both: " )
            
            # Edit name and number if chosen:
            if option == "b":                
                
                # Iterate through dictionary to find name then change name and number.
                for contact in self.contact_list:            
                    if contact["name"].lower() == name.lower():
                            new_name = input("Enter new name: ")
                            new_number = input("Enter new number: ")
                            contact["name"] = new_name
                            contact["number"] = new_number
                            print("\n** Contact changed **\n")
                            print(f"name: {contact['name']}\n")
                            print(f"number: {contact['number']}\n")                                                
            
            # Edit name if chosen:
            elif option == "na":                
                
                # Iterate through dictionary to find and change name.
                for contact in self.contact_list:            
                    if contact["name"].lower() == name.lower():
                            new_name = input("Enter new name: ")
                            contact["name"] = new_name
                            print("\n** Contact changed **\n")
                            print(f"name: {contact['name']}\n")
                            print(f"number: {contact['number']}\n")                                                                            
        
            # Edit number if chosen:            
            elif option == "nu":                
                
                # Iterate through dictionary to find name then change number.
                for contact in self.contact_list:            
                    if contact["name"].lower() == name.lower():                                                                                                    
                            
                        while True:

                                # Catch error and display message if string added to 'number' section.
                                try:
                                    new_number = int(input("Enter new number: "))
                                    contact["number"] = new_number
                                    print("\n** Contact changed **\n")
                                    print(f"name: {contact['name']}\n")
                                    print(f"number: {contact['number']}\n")
                                    break
                            
                                except ValueError:
                                    print("\n! You need to enter digits !\n")                                
                                        
            # Write the updated contact list to .txt file.        
            self.write_to_txt_file("contacts.txt")
        
            # Make sure self.contact_list matches .txt file. 
            self.update_contact_list("contacts.txt")

            # Return to main menu.
            main_menu.show_menu()

        # Invalid choice message:
        else: 
            print("\n!! Enter a valid choice !!\n")
    

    def delete_contact(self):
        '''Deletes contact details for given name.'''
        
        name = input("\nType the name of the contact that you would like to delete: ")                  

        # iterate through contacts then remove dictionary when name matched.
        for dict in self.contact_list:
            for value in dict.values():                                                
                if value.lower() == name.lower():
                    self.contact_list.remove(dict)
                    break
        
        # Displau confirmation message if using discrete delete method.
        if self.embedded_delete == False:
            print("\n\n** Contact deleted **\n\n")
            
        # Write the updated contact list to .txt file.        
        self.write_to_txt_file("contacts.txt")
        
        # Make sure self.contact_list matches .txt file. 
        self.update_contact_list("contacts.txt")
                
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

# Instantiate the phonebook class and initialise the contacts.txt document.                
my_phonebook = Phonebook("contacts.txt")

# Instantiate the main menu and view menu.
main_menu = Menu("Add a contact", "View contacts", "Search for a contact", "Exit", my_phonebook.add_contact, my_phonebook.view_contacts, 
                 my_phonebook.search, exit)

view_menu = Menu("Add a contact", "Edit a contact", "Delete a contact", "Home", my_phonebook.add_contact, my_phonebook.edit_contact, 
                my_phonebook.delete_contact, main_menu.show_menu)

# Display the main menu.
main_menu.show_menu()