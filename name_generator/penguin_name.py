penguin_converter = {
    "January": "Mumble ",
    "February": "Squeak",
    "March": "Skipper",
    "April": "Gloria",
    "May": "Kowalski",
    "June": "Rico",
    "July": "Private",
    "August": "King",
    "September": "Pingu",
    "October": "Emperor",
    "November": "Chocolatey",
    "December": "Ice Cold"
}

def user_penguin(first_name, birth_month):
    penguin_name = penguin_converter[birth_month]
    return penguin_name