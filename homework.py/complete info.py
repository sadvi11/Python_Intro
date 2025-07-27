def userinput():
    # Collect user details
    schoolname = input("Enter your school name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")

    # Display the final details
    print("\n--- Here are your details ---")
    print("School Name:", schoolname)
    print("Email:", email)
    print("Address:", address)

# Call the function
userinput()
