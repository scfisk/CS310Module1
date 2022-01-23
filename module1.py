import json

def open_file():
    try:
        with open("addresses.json") as address_list:
            addresses = json.load(address_list)
    except FileNotFoundError:
        print("File can't be opened.")
    return addresses

def get_address():
    new_address = input("Address: ")
    return new_address

def get_city():
    new_city = input("City: ")
    return new_city

def get_priority():
    new_priority = input("Priority: ")
    return new_priority

def address_found(address):
    print(address, " is already on your list.")
    return

def add_address(address, addresses):
    addresses.append(new_address)
    with open("addresses.json", "w") as address_list:
        json.dump(addresses, address_list, indent = 8)
    print(address, " has been added to your list.")
    return 

def compare_address(new_address, addresses):
    found = False
    for x in addresses:
        print(x)
        if x == new_address:
            address_found(new_address)
            found = True
    if found == False:
        add_address(new_address, addresses)
    return

addresses = open_file()
print(addresses)
new_address = {
    "Street Address": get_address(),
    "City": get_city(),
    "Priority": get_priority()
}
compare_address(new_address, addresses)

 
