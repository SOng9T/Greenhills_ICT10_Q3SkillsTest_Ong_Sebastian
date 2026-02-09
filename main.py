from pyscript import display, document
'''def account_authenticator(e): 
    document.getElementById("output").innerHTML = " "

    username = document.getElementById("name").value
    digits = document.getElementById("digits").value

    if username.isalpha():
        if digits.isdigit() and len(digits) == 4:
            document.getElementById("output").innerHTML = f"Welcome, {username}! Your digit is {digits}."
        else:
            document.getElementById("output").innerHTML = "Invalid!"
    else:
        document.getElementById("output").innerHTML = "Invalid username. Please use only letters."'''
def account_authenticator(e):

    document.getElementById("output").innerHTML = " "

    username = document.getElementById("name").value
    password = document.getElementById("digits").value

    #7 characters username
    if len(username) >= 7:

        # Password checks
        has_letter = any(char.isalpha() for char in password)
        has_number = any(char.isdigit() for char in password)

        #for 10 characters
        if len(password) >= 10:

            # Password will contain at least one letter and one number for mr ortiz
            if has_letter and has_number:
                document.getElementById("output").innerHTML = f"Welcome, {username}! Account created successfully."
            else:
                document.getElementById("output").innerHTML = "Password must contain at least one letter and one number."

        else:
            document.getElementById("output").innerHTML = "Password must be at least 10 characters long."

    else:
        document.getElementById("output").innerHTML = "Username must be at least 7 characters."


