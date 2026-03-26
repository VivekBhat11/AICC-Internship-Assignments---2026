# Set a strong password first
correct_password = "Vivek@123"

# Ask user to enter password
user_password = input("Enter your password: ")

# Check if password is correct , if correct access granted 
if user_password == correct_password:
    print("Access Granted ✅")
else:
    print("Access Denied ❌")