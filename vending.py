class VendingMachine:
    def __init__(self):# initialises 2 elements 
        self.__Items = {# the menu of items available
            "Drinks": {
                'Drink1': {"Type": "Coca Cola", "Price": 4.65},
                'Drink2': {"Type": "Orange Juice", "Price": 2.21},
                'Drink3': {"Type": "Water", "Price": 3.45},
                'Drink4': {"Type": "Tea", "Price": 2.45},
                'Drink5': {"Type": "Coffee", "Price": 1.45},
            },
            "Snacks": {
                'Snack1': {"Type": "Chips", "Price": 1.0},
                'Snack2': {"Type": "Chocolate", "Price": 1.2},
                'Snack3': {"Type": "Biscuts", "Price": 8.2},
                'Snack4': {"Type": "Chicken puff", "Price": 11.2},
            },
        }
        self.__Balance = 0  # Keeps track of the amount of money the user has inserted

    def money(self):
        while True:
            try:
                amount = float(input("Insert money (AED): "))
                if amount > 0:
                    self.__Balance += amount
                    print(f"Your current balance is: AED {self.__Balance:.2f}")
                    break
                else:
                    print("Please insert a positive amount.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

    def choice(self): # allows users to select the item they want
        print("Available Items:")
        for category, items in self.__Items.items():
            print(f"{category}:")
            for code, details in items.items():
                print(f"  {code}: {details['Type']} - AED {details['Price']:.2f}")

        while True:
            item_code = input("Enter the item code of the item you would like: ")
            for category, items in self.__Items.items():
                if item_code in items:
                    item = items[item_code]
                    if self.__Balance >= item["Price"]:
                        self.__Balance -= item["Price"]
                        print(f"{item['Type']} dispensed. Remaining balance: AED {self.__Balance:.2f}")
                        return True
                    else:
                        print(f"Insufficient funds. {item['Type']} costs AED {item['Price']:.2f}.")
                        return False
            print("Invalid item code. Please try again.")

    def additional_items(self): # this gives suggestions to the users if they want more items
        while True:
            choice = input("Would you like to purchase another item? (yes/no): ").strip().lower()
            if choice in ["yes", "no"]:
                return choice == "yes"
            print("Invalid input. Please enter 'yes' or 'no'.")

    def change(self):# tells them the change they will recieve 
        if self.__Balance > 0:
            print(f"The balance to be returned is: AED {self.__Balance:.2f}")
            self.__Balance = 0
        else:
            print("No change to return.")

    def run(self):
        print("Welcome to the Vending Machine!")
        while True:
            self.money()
            while True:
                if not self.choice():
                    continue
                if not self.additional_items():
                    break
            self.change()
            print("Thank you for using the Vending Machine!")
            break


# call the vending machine
vm = VendingMachine()
vm.run()