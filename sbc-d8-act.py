info_users = {}  

def save_users_info():
    with open("user_info.txt", "w") as file:
        file.writelines([f"{username},{password}\n" for username, password in info_users.items()])

def load_users_info():
    try:
        with open("user_info.txt", "r") as file:
            info_users.update({username: password for username, password in (line.strip().split(',') for line in file)})
    except FileNotFoundError:
        pass

load_users_info()  
def register():
    username = input("Enter a username: ")
    if username in info_users:
        print("Username already exists. Please choose a different username.")
        return
    password = input("Enter a password: ")
    info_users[username] = password
    save_users_info()  
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if info_users.get(username) == password:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")

def change_password():
    username = input("Enter your username: ")
    if username in info_users:
        current_password = input("Enter your current password: ")
        if info_users[username] == current_password:
            new_password = input("Enter your new password: ")
            info_users[username] = new_password
            save_users_info() 
            print("Password changed successfully!")
        else:
            print("Incorrect current password. Password change failed.")
    else:
        print("Username not found. Please register or enter a valid username.")

def save_user_info_to_file():
    save_choice = input("Do you want to save your account information to a file? (yes/no): ")
    if save_choice.lower() == 'yes':
        save_users_info()
        print("Account information saved to file.")
    else:
        print("Account information not saved.")

while True:
    print("\nUser Login System\n1. Register\n2. Login\n3. Change Password\n4. Save Account Info to File\n5. Exit")
    choice = input("Enter your choice (1-5): ")
    actions = {'1': register, '2': login, '3': change_password, '4': save_user_info_to_file}
    if choice in actions:
        actions[choice]()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please select a valid option.")