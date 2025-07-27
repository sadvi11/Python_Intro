username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful!")
elif username != "admin":
    print("Invalid username.")
else:
    print("Incorrect password.")
