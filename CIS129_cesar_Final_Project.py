# Module_13-Final_Project
# author-cesar
# date-2025-05-06
"""
Pseudocode Outline
TIM - Traveling Inventory Management
"""

"""
main()

    Display startup message
    “Inventory Opened”

    Create a new dictionary to hold item-quantities entries
    or
    Read a saved file to display current inventory contents 

        Inventory Name e.g. “Backpack”
        ----------------------------------
        Phone           |1
        Charger brick   |2
        Charger cable   |3
        tshirt          |3
        pants           |2
        etc…            |etc…
        ----------------------------------

    Loop to receive new items and their quantities, or to update/remove entries
        itemName = input(“Enter name of item to add: (leave blank to cancel)”)
        If blank, exit loop
        itemQuantity = input(“Enter quantity for item: “)
        
        inventory[itemName] = itemQuantity
        Display 
    “Item {itemName} added”

    Write a CSV file to store inventory data
            Open inventoryName.csv
            Write itemName, itemQuantity
                For each item, quantity in inventoryName
        Display
            “Inventory saved to inventoryName.csv”
"""