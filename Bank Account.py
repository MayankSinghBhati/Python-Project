#-----------------------------------------------------------------------Dictionary to store user details--------------------------------------------------------------
details = {
    'mayank': {'pas': 2425, 'Father name': 'ABC', 'Blood group': 'B+', 'balance': 1023857, 'loan': 823},
    'sarvgya': {'pas': 5325, 'Father name': 'XYZ', 'Blood group': 'O+', 'balance': 2, 'loan': 1221124},
}

#-----------------------------------------------------------------------Create account function-----------------------------------------------------------------------
def create_account():
    Register = input('Enter a new username: ')
    if Register in details:
        print('The username is already registered, try again')
    else:
        newpass = input('Enter password (4 digits): ')
        Father_name = input('Enter Father name: ')
        Blood_group = input('Enter Blood Group: ')
        details[Register] = {
            'pas': int(newpass),
            'Father name': Father_name,
            'Blood group': Blood_group,
            'balance': 0,
            'loan': 0
        }
        print(f"Account created for {Register}!")
    return login()  # Return to login after account creation

#-----------------------------------------------------------------------Login function-----------------------------------------------------------------------
def login():
    while True:
        username = input('Enter username: ')
        if username in details.keys():
            password = int(input('Enter password: '))
            if password == details[username]['pas']:
                main_screen(username)  # After login, proceed to the main screen
                break
            else:
                print('Incorrect password, try again')
        else:
            print('The username is not found')
            confirmation = input('Do you want to register a new account? Type y or n: ').lower()
            if confirmation == 'y':
                create_account()
                break
            else:
                print('---------------------------- Enjoy :) ----------------------------')
                break

# -----------------------------------------------------------------------Main screen function-----------------------------------------------------------------------
def main_screen(username):
    print('''---------------------------- 
Logged in successfully
Type below numbers to continue - 
Loans - 1
Balance - 2
Profile - 3 
---------------------------- 
''')
    
    newconfirmation = input("Enter your choice: ")
    
    if newconfirmation == '1':
        loans(username)

    elif newconfirmation == '2':
        print(f"Your current balance is: {details[username]['balance']}")
    
    elif newconfirmation == '3':
        update_details(username)
    else:
        print("Invalid option. Please try again.")
        main_screen(username)

#-----------------------------------------------------------------------Update details-----------------------------------------------------------------------
def update_details(username):
    print('''----------
Press number to access below -
1 to see profile details
2 to update profile
3 to go back to main screen    
----------''')
    x = int(input())
    
    if x == 1:
        # Print the user's profile details
        print(f"Username: {username}")
        print(f"Password: {details[username]['pas']}")
        print(f"Father Name: {details[username]['Father name']}")
        print(f"Blood Group: {details[username]['Blood group']}")
    
    elif x == 2:
        print('''Press 1 to reset password 
Press 2 to change Father name
Press 3 to change Blood group
''')
        Key_pressed = int(input())
        pas_confirm = int(input('Enter current password: '))
        
        # Check if the entered password is correct before allowing updates
        while pas_confirm != details[username]['pas']:
            print('Incorrect password, try again')
            pas_confirm = int(input('Enter current password: '))

        if Key_pressed == 1:
            new_pas = int(input('Enter new password: '))
            details[username]['pas'] = new_pas
            print("Password updated successfully!")
        
        elif Key_pressed == 2:
            new_father_name = input('Enter new Father name: ')
            details[username]['Father name'] = new_father_name
            print("Father name updated successfully!")
        
        elif Key_pressed == 3:
            new_blood_group = input('Enter new Blood group: ')
            details[username]['Blood group'] = new_blood_group
            print("Blood group updated successfully!")
    
    elif x == 3:
        main_screen(username)

#-----------------------------------------------------------------------Loans------------------------------------------------------------------------------------------------
def loans(username):
    print('''----------
Check loan taken - 1
Take loan - 2
----------''')
    loan_option = input("Enter your choice: ")
    if loan_option == '1':
        print(f"Your current loan is: {details[username]['loan']}")
    elif loan_option == '2':
        new_loan = int(input('Enter the amount to take as loan: '))
        details[username]['loan'] += new_loan  # Correct loan update
        details[username]['balance'] += new_loan  # Update balance after loan
        print(f"New loan balance is: {details[username]['loan']}")

#-----------------------------------------------------------------------Main program starts-----------------------------------------------------------------------
print('----------Welcome to Apna Bank----------')
login()
