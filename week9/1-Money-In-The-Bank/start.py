import sql_manager
import getpass


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")

    while True:
        command = input("$$$>")
        if command == 'register':
            register()
        elif command == 'login':
            login()
        elif command == 'help':
            help1()
        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())

    while True:
        command = input("Logged>>")
        if command == 'info':
            info(logged_user)
        elif command == 'changepass':
            changepass(logged_user)
        elif command == 'change-message':
            change_message()
        elif command == 'show-message':
            print(logged_user.get_message())
        elif command == 'help':
            help2()
        elif command == 'logout':
            break


def register():
    username = input("Enter your username: ")
    password = getpass.getpass(prompt="Enter your password: ")

    while invalid_password(username, password):
        password = getpass.getpass(prompt="Your password must be longer than 8 characters, must contain both upper- and lowercase letter, number and a special symbol!\nAlso it shouldn't contain your username!\nEnter your password: ")

    sql_manager.register(username, password)

    print("Registration Successfull")


def invalid_password(username, password):
    if username in password:
        return True
    elif len(password) < 8:
        return True
    elif password.isupper() or password.islower() or password.isdigit() or password.isalpha() or password.isalnum():
        return True
    return False



def login():
    username = input("Enter your username: ")
    password = getpass.getpass(prompt="Enter your password: ")

    logged_user = sql_manager.login(username, password)

    if logged_user == -2:
        print("There is no such username")
    elif logged_user == -1:
        print("Sorry you have to wait 5 minutes for another 5 tries.")
    elif logged_user == 0:
        print("Wrong password")
    else:
        logged_menu(logged_user)


def help1():
    print("login - for logging in!")
    print("register - for creating new account!")
    print("exit - for closing program!")


def info(logged_user):
    print("You are: " + logged_user.get_username())
    print("Your id is: " + str(logged_user.get_id()))
    print("Your balance is:" + str(logged_user.get_balance()) + '$')


def changepass(logged_user):
    new_pass = input("Enter your new password: ")
    sql_manager.change_pass(new_pass, logged_user)


def change_message(logged_user):
    new_message = input("Enter your new message: ")
    sql_manager.change_message(new_message, logged_user)


def help2():
    print("info - for showing account info")
    print("changepass - for changing passowrd")
    print("change-message - for changing users message")
    print("show-message - for showing users message")


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
