# Angela Holden
#
# HW 8-3: inventory.py
#
#   Solution code (mostly) for a simple inventory tracking program
#     using dictionaries.
#

def getCommand():
    command = input("Enter command: ")
    return command

def addToInventory(dict):
    invname = input("Enter name of item to add to inventory: ")
    qty = int(input("Enter quantity of item to add: "))

    dict[invname] = dict.get(invname, 0) + qty

def viewInventory(dict):
    print("%9s -- %s" % ("Item", "Qty"))
    for (k, v) in dict.items():
        print("%9s -- %d" % (k, v))

def deleteInventory(dict):
    itemtormv = input("Enter name of item to remove from inventory: ")
    if itemtormv in dict:
        amt = int(input("Enter the quantity to remove: "))
        if amt > dict[itemtormv]:
            print("Exceeds available amount.", dict[itemtormv], itemtormv, "available to remove.")
        elif amt == dict[itemtormv]:
            del dict[itemtormv]
            print(itemtormv.capitalize(), "deleted!")
        else:
            dict[itemtormv] = dict.get(itemtormv, 0) - amt
            print(amt, itemtormv, "removed.", dict.get(itemtormv), itemtormv, "in inventory.")
    else:
        print(itemtormv.capitalize(), "not in inventory.")

def main():

    print("Welcome to StuffMaster, v.0.47")

    inventory = {}  # empty dictionary

    while True:  # get command, process command; quit when selected below

        print("Commands are: ")
        print("'A' => Add to inventory")
        print("'V' => View existing inventory")
        print("'D' => Delete from inventory")
        print("'Q' => Quit after showing final inventory")

        # Get the command

        cmd = getCommand().upper()[0]

        # Call the appropriate function based on command

        if cmd is 'A':
            addToInventory(inventory)
        elif cmd is 'V':
            viewInventory(inventory)
        elif cmd is 'D':
            deleteInventory(inventory)
        elif cmd is 'Q':
            break
        else:
            print("Unknown command: %s => try again." % cmd)

        # If unknown command, complain and prompt for reentry

    # here, we're quitting

    print("Quitting. Final version of inventory is:")

    # print out final version of inventory

    viewInventory(inventory)

    print("Exiting...")


main()
