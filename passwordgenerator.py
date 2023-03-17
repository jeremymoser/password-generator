import random, string

min_length = int(input("Enter the minimum password length: "))
has_number = input("Do you want the password to include numbers? (y/n) ").lower() == "y"
has_special = input("Do you want the password to include special characters? (y/n) ").lower() == "y"

def generate_password(min_length, numbers, special_characters):
    letters = string.ascii_letters
    nums = string.digits
    special_chars = string.punctuation

    charset = letters
    if numbers:
        charset += nums
    if special_characters:
        charset += special_chars

    meets_criteria = False
    password = ""
    has_number = False
    has_special = False
    
    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(charset)
        password += new_char

        if new_char in nums:
            has_number = True
        if new_char in special_chars:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
        
    return password

generated_password = generate_password(min_length, has_number, has_special)
print("The generated password is:", generated_password)
print("Generated password has", len(generated_password), "character(s)")