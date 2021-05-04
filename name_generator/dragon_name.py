dragon_converter = {
    "January": "Blaze",
    "February": "Fuego",
    "March": "Charmander",
    "April": "Drogan",
    "May": "Viserion",
    "June": "Rheagal",
    "July": "Draco",
    "August": "Rex",
    "September": "Puff",
    "October": "Yoshi",
    "November": "Norbert",
    "December": "Charizard"
}

def user_dragon(first_name, birth_month):
    dragon_name = dragon_converter[birth_month]
    return dragon_name