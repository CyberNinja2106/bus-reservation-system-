import getpass

# Sample credentials (You can modify or extend this)
USER_CREDENTIALS = {"admin": "1234", "user": "pass","hitu":"2106"}

passengers = []

bus_data = {
    "Kutch Express": {"Source": "Godhra", "Destination": "Kutch", "Price": 2000},
    "Air Express": {"Source": "Godhra", "Destination": "Dahod", "Price": 1000},
    "Seen Express": {"Source": "Godhra", "Destination": "Anand", "Price": 3000},
    "Water Express": {"Source": "Godhra", "Destination": "Porbandar", "Price": 4000},
    "Fire Express": {"Source": "Godhra", "Destination": "Kalol", "Price": 500},
    "Let Express": {"Source": "Godhra", "Destination": "Vadodara", "Price": 3500}
}

def show_available_buses():
    print("\nLIST OF ALL BUSES")
    print(f"{'Name':<20}{'Source':<15}{'Destination':<15}{'Price':>10}")
    print("-" * 60)
    
    for bus, details in bus_data.items():
        print(f"{bus:<20}{details['Source']:<15}{details['Destination']:<15}{details['Price']:>10}")

def book_ticket():
    total_price = 0
    try:
        num_tickets = int(input("Enter the number of tickets you want to book: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    for _ in range(num_tickets):
        passenger = {}
        passenger["Name"] = input("Enter passenger name: ")
        try:
            passenger["Age"] = int(input("Enter passenger age: "))
        except ValueError:
            print("Invalid age! Please enter a number.")
            return

        passenger["Destination"] = input("Enter destination: ")
        found_bus = next((bus for bus, details in bus_data.items() if details["Destination"] == passenger["Destination"]), None)

        if found_bus:
            passenger["Price"] = bus_data[found_bus]["Price"]
            total_price += passenger["Price"]
            passengers.append(passenger)
        else:
            print("Please enter a valid destination.")
    
    print(f"Your total ticket price is {total_price}")

def delete_ticket():
    if not passengers:
        print("No tickets booked yet. Please book a ticket first.")
        return

    passenger_name = input("Enter passenger name to delete the ticket: ")
    found_passenger = next((p for p in passengers if p["Name"] == passenger_name), None)

    if found_passenger:
        passengers.remove(found_passenger)
        print(f"Ticket for {passenger_name} has been deleted successfully.")
    else:
        print(f"No ticket found for passenger {passenger_name}.")

def view_ticket():
    if not passengers:
        print("No tickets booked yet.")
        return

    print("\n-----Bus Ticket-----")
    for passenger in passengers:
        print(f"Name: {passenger['Name']}")
        print(f"Age: {passenger['Age']}")
        print(f"From: Godhra")
        print(f"To: {passenger['Destination']}")
        print(f"Price: {passenger['Price']}")
        print("--------------------")

def login():
    print("\n" + "="*50)
    print("WELCOME TO BUS RESERVATION SYSTEM".center(50))
    print("="*50)

    while True:
        username = input("\nEnter Username: ")
        password = getpass.getpass("Enter Password: ")  # Hides password input

        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            print("\nLogin Successful! Welcome, {}!".format(username))
            break
        else:
            print("Invalid credentials! Please try again.")

# Main menu
login()  # Call login function before accessing the system

while True:
    print("\n-----BUS RESERVATION SYSTEM-----")
    print("1: Show all available buses")
    print("2: Book a ticket")
    print("3: Delete a ticket")
    print("4: View your ticket")
    print("5: Exit")
    choice = input("Enter a number between 1 to 5: ")

    if choice == '1':
        show_available_buses()
    elif choice == '2':
        book_ticket()
    elif choice == '3':
        delete_ticket()
    elif choice == '4':
        view_ticket()
    elif choice == '5':
        print("Thank you for using our system. Have a safe journey!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
