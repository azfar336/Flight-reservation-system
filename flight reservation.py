import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="your_password",database="flight_db")
cur = con.cursor()

def signup():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    query = "INSERT INTO passengers VALUES (%s, %s)"
    values = (username, password)
    cur.execute(query, values)
    con.commit()
    print("SignUp Successful")

def signin():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    query = "SELECT * FROM passengers WHERE username=%s AND password=%s"
    values = (username, password)
    cur.execute(query, values)
    data = cur.fetchone()
    if data:
        print("SignIn Successful")
        passenger_menu(username)
    else:
        print("Invalid Username or Password")
        
def check_availability():
    print("\nAvailable Flights")
    print("1. Air India - Chennai to Delhi")
    print("2. Indigo - Chennai to Mumbai")
    print("3. Vistara - Chennai to Bangalore")

def book_ticket(username):
    flight = input("Enter Flight Name: ")
    source = input("Enter Source: ")
    destination = input("Enter Destination: ")
    query = """
    INSERT INTO tickets(username, flight_name, source, destination, status)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (username, flight, source, destination, "Pending")
    cur.execute(query, values)
    con.commit()
    print("Ticket Booked Successfully")
    print("Status: Pending")

def cancel_ticket(username):
    ticket_id = int(input("Enter Ticket ID to Cancel: "))
    query = "DELETE FROM tickets WHERE ticket_id=%s AND username=%s"
    values = (ticket_id, username)
    cur.execute(query, values)
    con.commit()
    print("Ticket Cancelled Successfully")

def status_checking(username):
    query = "SELECT * FROM tickets WHERE username=%s"
    values = (username,)
    cur.execute(query, values)
    data = cur.fetchall()
    for row in data:
        print(row)

def passenger_menu(username):
    while True:
        print("\nPassenger Menu")
        print("1. Check Availability")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. Status Checking")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            check_availability()
        elif choice == 2:
            book_ticket(username)
        elif choice == 3:
            cancel_ticket(username)
        elif choice == 4:
            status_checking(username)
        elif choice == 5:
            break
        else:
            print("Invalid Choice")

def approve_ticket():
    ticket_id = int(input("Enter Ticket ID to Approve: "))
    query = "UPDATE tickets SET status=%s WHERE ticket_id=%s"
    values = ("Approved", ticket_id)
    cur.execute(query, values)
    con.commit()
    print("Ticket Approved Successfully")

def cashier_cancel_ticket():
    ticket_id = int(input("Enter Ticket ID to Cancel: "))
    query = "UPDATE tickets SET status=%s WHERE ticket_id=%s"
    values = ("Cancelled", ticket_id)
    cur.execute(query, values)
    con.commit()
    print("Ticket Cancelled by Cashier")

def cashier_menu():
    while True:
        print("\nCashier Menu")
        print("1. Approve Ticket")
        print("2. Cancel Ticket")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            approve_ticket()
        elif choice == 2:
            cashier_cancel_ticket()
        elif choice == 3:
            break
        else:
            print("Invalid Choice")

while True:
    print("\nFlight Reservation System")
    print("1. Passenger")
    print("2. Cashier")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("\n1. SignUp")
        print("2. SignIn")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            signup()
        elif ch == 2:
            signin()
        else:
            print("Invalid Choice")

    elif choice == 2:
        cashier_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Choice")
con.close()
