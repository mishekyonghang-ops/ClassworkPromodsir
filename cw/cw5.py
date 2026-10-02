username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "admin":
    role = "Administrator"
    print(f"Role: Administrator")
    if role == "Administrator":
        print("Full system access.")
    elif role == "Student":
        print("Student access.")

elif username == "student12" and password == "study123":
    role = "Student"
    print(f"Role: {role}")
    if role == "Administrator":
        print("Full system access.")
    elif role == "Student":
        print("Student access.")

else:
    print("Invalid username or password.")