# Add a view menu method that displays all contacts underneath sub-menu (sorted: special dictionary?) - home
# Add a view sub-menu method -search -edit contact -delete contact -back -home
# Add an edit sub-menu -edit name -edit number -back -home

# ***save the above notes in publisher app structure file, along with notes on classes***

# Instantiate my_phonebook


## TO DO:
# \n split fault 
import os

class Menu:        

    def show_main_menu(self):
        '''Displays main menu for user and task-related tasks.'''  
        while True:
        # presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
              print()
              menu = input('''Select one of the following Options below:          
          a - Add a contact
          v - View contacts
          s - Search for a contact                 
          e - Exit
          : ''').lower()

              menu

              if menu == 'a':
                  self.show_add_menu()                  

              elif menu == 'v':
                  self.show_view_menu()
              
              elif menu == 's':
                  name = input("Name: ")
                  my_phonebook.search(name)                              
            
              else:
                  print("\n!! Choose a valid option. !!\n")
                  
                  
    def show_view_menu(self):
        '''Displays sub menu for viewing contacts'''
        my_phonebook.view_contacts()
                  
    def show_add_menu(self):
        '''Displays sub menu for adding a contact'''
        while True:
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            
            if len(number) > 11:
                print("!! You have entered too many digits. Try again !!")

            else:
                # Save the name and number to a .txt file.
                my_phonebook.add_contact(name, number)                
                print("\n***Contact has been saved***\n")
                break
        
class Phonebook:
    
    contact_list = []
    
    def __init__(self, txt_file):
        self.txt_file = txt_file
           
        # Create the .txt file if it doesn't exist 
        if not os.path.exists(txt_file):
            with open(txt_file, "w") as default_file:
                pass
            
    def add_contact(self, name, number):
        '''adds new contact to the contact_list class variable'''
        
        new_contact = {
            "name": name,
            "number": number
        }
        
        self.contact_list.append(new_contact)
        self.write_to_txt_file("contacts.txt")
        self.save("contacts.txt")
    
    def view_contacts(self):
        self.save("contacts.txt")        
        for dict in self.contact_list:            
            for value in dict.values():
                try: 
                    value != ""                    
                    print(f"******\tname: {dict['name']}\t ******\n")
                    print(f"******\tnumber: {dict['number']}\t ******\n\n")
                    break
                except:
                    print("\n!! You have not added a contact yet !!\n")
        
    def search(self, name):
        self.save("contacts.txt")        
        for dict in self.contact_list:            
            for value in dict.values():
                try: 
                    value.lower() == name.lower()
                    print("\n** Contact found! **\n")
                    print(f"name: {dict['name']}\n")
                    print(f"number: {dict['number']}\n")
                    break
                except:
                    print("\n!! This contact has not yet been added !!\n")

    def write_to_txt_file(self, txt_file):
        '''Writes changes made to the tasks in task_list to a .txt file.'''
        with open(txt_file, "w") as contacts_file:
            contacts_list_to_write = []
            for c in self.contact_list:
                str_attrs = [
                    c['name'],
                    c['number']                    
                ]
                contacts_list_to_write.append(";".join(str_attrs))
            contacts_file.write("\n".join(contacts_list_to_write))

    def save(self, txt_file):
        '''Saves an the updated .txt file to the class variable contact_list.'''
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

                # Save each contact in an array of dictionaries.                                                  
                self.contact_list.append(curr_contacts)                    
                
my_menu = Menu()
my_phonebook = Phonebook("contacts.txt")
my_menu.show_main_menu()