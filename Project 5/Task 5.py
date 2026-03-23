#create a decorator that check login func with proper user credentials agr credentials shi hue to func call hoga vrna nhi hoga
USERS = {
    "admin": "1234",
    "luna": "python"
}
def login_required(func):
    n=int(input("Enter number of times you want to login: "))

    def wrapper(username, password):
        if username in USERS and USERS[username] == password:
            print("✅ Login successful")
            func()
        else:
            print("Invalid credentials. Access denied.")

    return wrapper

@login_required
def dashboard():
    print("Welcome to dashboard")

user_name = input("Enter username: ")
user_password = input("Enter password: ")
dashboard(user_name, user_password)
