import sqlite3
conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS passwords (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               username TEXT NOT NULL
               password TEXT NOT NULL
               )
''')

def list_password():
    cursor.execute("SELECT * FROM passwords")
    print('\n' + 60 * '*')
    for row in cursor.fetchall():
        print(f"{row[0]}. Service -> {row[1]} , Username -> {row[2]} , Password -> {row[3]}")
    print(60 * '*')

def add_password(name, username, password):
    cursor.execute("INSERT INTO passwords (name, username, password) VALUES (?, ?)", (name, username, password))
    conn.commit()

def update_password(service_id, new_name, new_username, new_password):
    cursor.execute("UPDATE passwords SET name = ?, username = ?, password = ? WHERE id = ?", (new_name, new_username, new_password, service_id))
    conn.commit()

def delete_password(service_id):
    cursor.execute("DELETE FROM passwords WHERE id = ?", (service_id,))
    conn.commit()

def main():
    while True:
        print("\n Password Manager | choose an option ")
        print("1. List all passwords ")
        print("2. Add a password ")
        print("3. Update a password details ")
        print("4. Delete a password ")
        print("5. Exit the app ")
        choice = input("Enter your choice : ")

        if choice == '1':
            list_password()
        elif choice =='2':
            name = input("Enter service name : ")
            username = input("Enter your username : ")
            password = input("Enter your password : ")
            add_password(name, username, password)
        elif choice =='3':
            list_password()
            servive_id = input("Enter service ID to update : ")
            name = input("Enter service name : ")
            username = input("Enter your username : ")
            password = input("Enter your password : ")
            update_password(servive_id, name, username, password)
        elif choice =='4':
            list_password()
            service_id = input('Enter service ID to delete : ')
            delete_password(service_id)
        elif choice == '5':
            break
        else:
            print("Invalid Option! Please try again")

    conn.close()

if __name__ ==  "__main__":
    main() 