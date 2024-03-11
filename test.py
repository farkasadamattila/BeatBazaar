def display_menu():
    print("Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")

def get_user_choice():
    choice = input("Enter your choice: ")
    return choice

def process_choice(choice):
    if choice == "1":
        print("Option 1 selected")
        # Add your code for Option 1 here
    elif choice == "2":
        print("Option 2 selected")
        # Add your code for Option 2 here
    elif choice == "3":
        print("Option 3 selected")
        # Add your code for Option 3 here
    elif choice == "4":
        print("Exiting...")
        # Add any cleanup code here if needed
    else:
        print("Invalid choice")

# Main program loop
while True:
    display_menu()
    user_choice = get_user_choice()
    process_choice(user_choice)
    if user_choice == "4":
        break