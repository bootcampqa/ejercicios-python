# Convert the amount to dolars and pounds

def convert_from_euros_to_dolars(euros_amount):
    result = euros_amount * 1.1
    return result

def convert_from_euros_to_pounds(euros_amount):
    result = euros_amount * 0.87
    return result

    

# Ask the user for an amount in euros
def conversor ():
    quantity_in_euros = float(input("Enter a quantity price in euros: "))

    print("Convert to Dollars")
    quantity_in_dollars = convert_from_euros_to_dolars(quantity_in_euros)
    print(quantity_in_dollars)

    print("Convert to Pound")
    print(convert_from_euros_to_pounds(quantity_in_euros))



conversor()