import json 

Phonebook = {}

def find_contact(name, area):
    contacts = {}
    if area == "*":
        for area in Phonebook:
            if name in Phonebook[area].keys():
                contacts[area] = Phonebook[area][name]
    else:
        if area in Phonebook.keys():
            if name in Phonebook[area].keys():
                contacts[area] = Phonebook[area][name]
            else:
                return {}
        else:
            return {}
    
    return contacts

def add_contact(name, number, area):
    if area not in Phonebook.keys():
        print("New Area")
        arealist = {}
        arealist[name] = number
        Phonebook[area] = arealist
    
    else:
        arealist = Phonebook[area]
        
        if name not in arealist.keys():
            arealist[name] = number
        else:
            if input("Contact already exists would you like to replace it:\t") == 'y':
                arealist[name] = number
    print("Contact Added")

add_contact("Ashish", 10378488, "Al Qusais")
add_contact("Ajin", 10538488, "Al Qusais")
add_contact("Thomas", 16038488, "Al Qusais")

add_contact("BOB", 1037458488, "burdubai")
add_contact("The", 1053853488, "burdubai")
add_contact("Builder", 1605438488, "burdubai")


while True:
    op = input("What would you like to do:\n 1) Add/Change Contact\n 2) Find Contact\n 3) Print Phonebook\n --> ")
    
    if op == "1":
        name = input("Name of Contact:\t")
        number = int(input("number of Contact:\t"))
        area = input("area of Contact:\t")
        add_contact(name, number, area)
        
    elif op == "2":
        name = input("Enter Name:\t")
        area = input("Enter Area(* to search all areas):")
        contact = find_contact(name, area)
        print(json.dumps(contact, indent=4))
        
    elif op == "3":
        print(json.dumps(Phonebook, indent=4))
