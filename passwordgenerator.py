import random, string

# While loop to test if password_length is an integer
while True:
    # User input for requested length of password
    try:
        password_length = int(input("Enter the number of password character(s): "))
    # If password_length is not an integer, the following message is displayed, and while loop restarts
    except:
        print(">> Invalid entry - please enter a number.")
        continue
    # If password_length is not an a positive integer, the following message is displayed, and while loop restarts
    if password_length <= 0:
        print(">> Invalid entry - please enter a positive number.")
        continue        
    # If all conditions are met, while loop stops
    else:
        break

# User input "Y" or "y" equals True, all else equals False
has_numbers = bool(input("Do you want the password to include numbers? (y/n) ").lower() == "y")
# User input "Y" or "y" equals True, all else equals False
has_specials = bool(input("Do you want the password to include special characters? (y/n) ").lower() == "y")

def generate_password(req_length, req_numbers, req_specials):
    # Upper and lower case alphabet chracters
    alphabet_chars = string.ascii_letters
    # Numberic characters
    numeric_chars = string.digits
    # Special characters
    special_chars = string.punctuation

    charset = alphabet_chars
    if req_numbers:
        charset += numeric_chars
    if req_specials:
        charset += special_chars

    # While loop variables initial values set
    meets_criteria = False
    password = ""
    has_numbers = False
    has_specials = False

    # Until the meets_criteria returns a True value and the generated password is not less than the users's requested length, the while loop iterates
    while not meets_criteria or len(password) < req_length:
        # Random selection of new_char from the charset
        new_char = random.choice(charset)
        # new_char added to generated password
        password += new_char
        # FOR TESTING PURPOSES: Uncomment the line below to watch the password generation process
        # print(f"Iterative password: {password}")

        # When the first numbers is added to the generated password, the has_numbers boolean is set to True
        if has_numbers is False and new_char in numeric_chars:
            has_numbers = True
            # FOR TESTING PURPOSES: Uncomment the line below to see when the has_numbers boolean value changes
            # print("has_number set to True")
        # When the first special character is added to the generated password, the has_specials boolean is set to True
        if has_specials is False and new_char in special_chars:
            has_specials = True
            # FOR TESTING PURPOSES: Uncomment the line below to see when the has_specials boolean value changes
            # print("has_specials set to True")

        meets_criteria = True
        # If the user requested numeric characters, it adds the has_numbers to the meets_criteria
        if req_numbers:
            meets_criteria = has_numbers
        # If the user requested special characters, it adds the has_specials to the meets_criteria
        if req_specials:
            meets_criteria = meets_criteria and has_specials
        # If the generated password length is more (greater than) the requested length, it resets the variables values and restarts the loop
        if len(password) > req_length:
            password = ""
            has_numbers = False
            has_specials = False
            continue

    # Return the generated password
    return password

# FOR TESTING PURPOSES: Uncomment the section below to see 20 instances of the requested password generated - adjust range based on your testing needs
"""
for i in range(20):
    generated_password = generate_password(password_length, has_numbers, has_specials)
    print(f">> #{i+1}) The generated password is: {generated_password} (Len: {len(generated_password)})")
"""

# Display the generated password
generated_password = generate_password(password_length, has_numbers, has_specials)
print(f">> Your {len(generated_password)} character generated password is: {generated_password}")