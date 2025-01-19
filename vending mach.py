import time      #importing the time  for delays
import random    #importing for generating random suggestions

print("WELCOME TO THE VENDING MACHINE ！\n") # Welcome message for the vending machine
time.sleep(1)   #PAUSE

menu = { #this is the menu for the vending machine
    "𝘚𝘕𝘈𝘊𝘒𝘚\n": [
        {"Item Name": "Chips", "Item no.": "1", "Price": 3, "Stock": 10},
        {"Item Name": "Protine Bar", "Item no.": "2", "Price": 5.5, "Stock": 15},
        {"Item Name": "Pop-Tarts", "Item no.": "3", "Price": 12, "Stock": 5},
        {"Item Name": "Chocolate Bars", "Item no.": "4", "Price": 20, "Stock": 9},
        {"Item Name": "Cheez-its", "Item no.": "5", "Price": 1.50, "Stock": 8}
    ],
    "𝘋𝘙𝘐𝘕𝘒𝘚\n": [
        {"Item Name": "Juice", "Item no.": "6", "Price": 2.5, "Stock": 7},
        {"Item Name": "Coke", "Item no.": "7", "Price": 5, "Stock": 5},
        {"Item Name": "Water", "Item no.": "8", "Price": 9.5, "Stock": 15},
        {"Item Name": "Coffee", "Item no.": "9", "Price": 15, "Stock": 3},
        {"Item Name": "Tea", "Item no.": "10", "Price": 14, "Stock": 4}
    ],
    "𝘉𝘈𝘒𝘌𝘙𝘠\n": [
        {"Item Name": "Cup cake", "Item no.": "11", "Price": 5, "Stock": 15},
        {"Item Name": "Chicken puff", "Item no.": "12", "Price": 3, "Stock": 8},
        {"Item Name": "Sandwich", "Item no.": "13", "Price": 4, "Stock": 8},
        {"Item Name": "Burger", "Item no.": "14", "Price": 5.5, "Stock": 5},
        {"Item Name": "Croissant", "Item no.": "15", "Price": 2.5, "Stock": 6}
    ]
        
}
def display_menu(menu):
    print("---------------𝑴 𝑬 𝑵 𝑼---------------")
    for menu, items in menu.items():    #loop each menu category 
        print(f"\n{menu}:")             #prints each category name
        for item in items:
            print(f" {item['Item no.']}. {item['Item Name']} - ${item['Price']} - (Stock: {item['Stock']})")  #prints the details by using the f-string function
    print("\n------------------------------------\n")

def buy_item(menu, item_number):
    for items in menu.values():         #loop through all categories
        for item in items:              #loop through each items in the category
            if item["Item no."] == item_number:   #checks if the item number matches
                return item             #returns the matching item
    return None                         #returns nothing id no items match

def suggest_purchase(menu, purchased_items):
    print(f"\nWould you like to buy some ")
    suggestions = [                   #list of items still in stock and not purchased
        item for items in menu.values()
        for item in items if item["Stock"] > 0 and item not in purchased_items
    ]
    if suggestions:
        suggestion = random.choice(suggestions)  #selects a random item
        print(f"- {suggestion['Item Name']} for ${suggestion['Price']}")
    else:
        print("\n- No suggestions available.")