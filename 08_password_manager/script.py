import json

def load_data():
    try:
        with open('password.txt', 'r') as file:
            passwordList = json.load(file)
            return passwordList
    except FileNotFoundError:
        return []

def save_password_helper(passwords):
    with open('password.txt', 'w') as file:
        json.dump(passwords, file)

def list_all_passwords(passwords):
    print(f'{50*'+'}')
    for index, password in enumerate(passwords, start=1):
        print(f"{index}. Service -> {password['name']} , Username -> {password['username']} , Password -> {password['password']}")
    print(f'{50*'+'}')

def add_password(passwords):
    name = input("Enter service name : ")
    username = input("Enter your username : ")
    password = input("Enter your password : ")
    passwords.append({'name': name, 'username': username, 'password': password})
    save_password_helper(passwords)
    print("Password added successfully!")

def update_password(passwords):
    list_all_passwords(passwords)
    index = int(input("Enter index of service : "))
    if 1 <= index <= len(passwords):
        name = input("Enter service name : ")
        username = input("Enter username : ")
        password = input("Enter password : ")
        passwords[index] = {'name' : name, 'username': username, 'password' : password}
        save_password_helper(passwords)
        print('Updated Sucsessfully!')
    else:
        print("Invaild Index!")


def delete_password(passwords):
    list_all_passwords(passwords)
    index = input('Enter the index of service to be deleted : ')
    if 1 <= index <= len(passwords):
        del passwords[index-1]
        print('Deleted Sucsessfully!')
        list_all_passwords(passwords)
    else:
        print("Invaild Index!")

def main():
    passwords = load_data()
    while True:
        print("\n Password Manager | choose an option ")
        print("1. List all passwords ")
        print("2. Add a password ")
        print("3. Update a password details ")
        print("4. Delete a password ")
        print("5. Exit the app ")
        choice = input("Enter your choice : ")

        match choice:
            case '1':
                list_all_passwords(passwords)
            case '2':
                add_password(passwords)
            case '3':
                update_password(passwords)
            case '4':
                delete_password(passwords)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ ==  "__main__":
    main() 