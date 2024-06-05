import os

class Menu:        

    def __init__(self, option_1, option_2, option_3, function_1, function_2, function_3, option_4=None, function_4=None):
        '''Displays main menu for user and task-related tasks.'''  
        while True:
        # presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
              print()
              menu = input(f'''Select one of the following Options below:          
          {[option_1[0].lower()]} - {option_1} 
          {[option_2[0].lower()]} - {option_2} 
          {[option_3[0].lower()]} - {option_3}           
          {[option_4[0].lower()]} - {option_4} 
          : ''').lower()

              menu

              if menu == [option_1[0]]:
                function_1# self.show_add_menu()                  

              elif menu == [option_2[0]]:
                function_2
                  
                  # Display contacts.
                  # my_phonebook.view_contacts()
                  
                  # Display sub-menu options after viewing contacts.
                  #self.show_view_menu()
              
              elif menu == [option_3[0]]:
                function_3
                  
                  # Update contact_list with latest contacts from saved .txt file.
                  #my_phonebook.update_contact_list("contacts.txt")  

                  # Error message if contact list is empty.
                  ###MOVE TO PHONEBOOK CLASS METHOD if my_phonebook.contact_list == []:
                    ###print("\n!! Your contacts list is empty !!\n")
                    
                  ###else:
                    ###name = input("\nName to search: \n")
                  
                    # Search contacts with name provided.
                    ###my_phonebook.search(name)
                  
                    # Display message if searched name matches a stored name.
                    ###if my_phonebook.search_success == True:
                        ###print("\n** Contact found **\n")                  
                        ###my_phonebook.search_success = False
                      
                        # Display sub-menu options.
                        ###self.show_search_menu(name)
                      
                    # Display message if searched name does not match a stored name.
                    ###else:
                        ###print("\n!! This contact has not yet been added !!\n")
              
              elif menu == [option_4[0]]:
                function_4
                #exit()
                
              else:
                  print("\n!! Choose a valid option. !!\n")
                  
                  
    def show_view_menu(self):
        '''Displays sub-menu for viewing contacts underneath listed contacts.'''        
        
        while True:
        # presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
              print()
              menu = input('''
          a - Add a contact                 
          e - Edit a contact
          d - Delete a contact
          h - Home          
          : ''').lower()
              if menu == 'a':
                  self.show_add_menu()
                  
              if menu == "e":                                    
                  my_menu.show_edit_menu()
                  
              elif menu == "d":
                  name = input("\nType the name of the contact that you would like to delete: ")
                  my_phonebook.delete_contact(name)
                  print("\n\n** Contact deleted **\n\n")
              
              elif menu == "h":
                  my_menu.show_main_menu()
              
              else:
                  print("\n!! Choose a valid option. !!\n")
    
    show_view_menu = Menu("Add a contact", "Edit a contact", "Delete a contact", option_4="Home", function_4=)

    def show_search_menu(self, name):
        '''Displays sub-menu for search results.'''                

        while True:
        # presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
              print()
              menu = input('''          
          e - Edit contact
          d - Delete contact
          h - Home          
          : ''').lower()
              if menu == 'e':
                  my_phonebook.edit_contact(name)
                  
              elif menu == 'd':
                  my_phonebook.delete_contact(name)
                  print("\n\n** Contact deleted **\n\n")
              
              elif menu == 'h':
                  my_menu.show_main_menu()
                  
              else:
                  print("\n!! Choose a valid option. !!\n")
              
                  

    def show_edit_menu(self):
        '''Displays sub-menu for editing contacts.'''
        while True:
            name = input("\nType the name of the contact that you would like to edit or type 'b' to go back: ")
            
            # Going one menu back if 'b' chosen
            if name.lower() == "b":
                my_menu.show_view_menu()
            else:
                my_phonebook.search(name)
                
                # Call edit method only if name is found.
                if my_phonebook.search_success == True:
                    my_phonebook.edit_contact(name)
                    
                    # Reset the successful search flag.
                    my_phonebook.search_success = False
                    
                else:
                    print("\n!! That contact has not yet been added !!\n")
                
                
    def show_add_menu(self):
        '''Displays sub-menu  for adding a contact'''
        #NOW ALL CONTAINED IN my_phonebook.add_contact
            
            
        
class Phonebook:
    
    contact_list = []
    search_success = False
    
    def __init__(self, txt_file):
        self.txt_file = txt_file
           
        # Create the .txt file if it doesn't exist 
        if not os.path.exists(txt_file):
            with open(txt_file, "w") as default_file:
                pass
            
    def add_contact(self, name, number):
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
                    
                    # Save the name and number to a .txt file if valid.
                    my_phonebook.add_contact(name, number)                
                    print("\n** Contact saved **\n")
                    break
            
            # Error capture if non-integer entered.                 
            except ValueError:
                print("\n!! You need to enter a number !!\n")

        # Make sure self.contact_list is updated
        self.update_contact_list("contacts.txt")

        # Search to check if contact already exists.
        self.search(name)
        
        # Issue error message if contact does exist.
        if self.search_success == True:
            print("\n!! This contact already exists. Pick a different name !!\n")            
            
            # Reset search_success flag.
            self.search_success = False
            
            # Return user to add_contact menu
            my_menu.show_add_menu()
        
        else:
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

    def search(self, name):
        '''Searches for a contact (by name) and then displays name and number.'''                      
        
        # Iterate through list of dictionaries to match seached name to value.
        #i = 0 # Counter variable.       
        for dict in self.contact_list:            
            for value in dict.values():                
                if value.lower() == name.lower():
                    self.search_success = True
                    print("\n------------------------\n")
                    print(f"\nname: {dict['name']}\n")
                    print(f"number: {dict['number']}\n")                    
                    print("\n------------------------\n")
                    break                                    
    
    def edit_contact(self, name):
        '''Allows the user to edit a name or contact.'''        
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
            my_menu.show_main_menu()

        # Invalid choice message:
        else: 
            print("\n!! Enter a valid choice !!\n")
    

    def delete_contact(self, name):
        '''Deletes contact details for given name.'''
        
        # iterate through contacts then remove dictionary when name matched.
        for dict in self.contact_list:
            for value in dict.values():                                                
                if value.lower() == name.lower():
                    self.contact_list.remove(dict)
                    break
                
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

# Instantiate the classes                
my_menu = Menu()
my_phonebook = Phonebook("contacts.txt")

# Call main menu method to give user main options on first screen.
my_menu.show_main_menu("Add a contact", "View contacts", "Search for a contact", "Exit")

