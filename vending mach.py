products_with_prices={
    "A1":("Apple",02.00),
    "A2":("Juice",01.50),
    "A3":("Chips", 02.50),
    "A4":("Biscuits", 05.00),
    "A5":("Ice cream", 02.50),
    "A6":("Tea", 01.00),
    "A7":("Chicken", 13.00),
    "A8":("Blueberries", 05.00),
    "A9":("Chocolate", 04.00),
    "A10":("Cake", 50.00),
    "A11":("Water", 02.50),
    "A12":("Candy",00.50)
    }
def display():
    print("\nAvailable Items:")
    for code,(name,price) in products_with_prices.items():
        print(f"{code}:{name}-${price:.2f}")