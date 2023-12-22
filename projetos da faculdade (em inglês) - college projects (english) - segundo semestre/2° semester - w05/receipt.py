import csv
from datetime import datetime

#   element in the inner dictionary
KEY_COLUMN_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

#   element in the inner listss
PRODUCT_CODE_INDEX = 0
NAME_INDEX = 1

#   Get the current date and time from your computer’s operating system.
current_date_and_time = datetime.now(tz=None)

def main():
    try:
        store_name = (f"Shop name: Inkom Emporium")

        #   stores the compound dictionary in a variable.
        products_dict = read_dictionary("2° semester - w05/products.csv", KEY_COLUMN_INDEX)
        print()
        print(f"{store_name}\n\nRequested Items")   # Receipt

        #   Open the products.csv file in VS Code and examine it.
        with open("2° semester - w05/request.csv") as request_file:
            #   read the request.csv file
            reader = csv.reader(request_file)
            #   Skipp the first line of the csv file
            next(reader)

            count = 0 # Viariable that will sum the total price to be paid.
            subtotal = 0
            number_items = 0
            sales_tax_rate = 0
            total = 0

            for request in reader: #The reader object returns each row as a list.
                # Use the requested product number to find the corresponding item in the products_dict.
                product_code = request[PRODUCT_CODE_INDEX]
                product_quantity = request[NAME_INDEX]
                
                for name, value in products_dict.items():
                    
                    #   Print the product name, requested quantity, and product price.
                    if product_code == name:
                    
                        name_product = value[PRODUCT_NAME_INDEX]
                        product_price = value[PRODUCT_PRICE_INDEX]

                        #   Sum and print the subtotal due.
                        count = float(product_price) * int(product_quantity)
                        subtotal += count

                        #   Sum and print the number of ordered items.
                        count = int(product_quantity)
                        number_items += count
                        
                        #   Compute and print the sales tax amount. Use 6% as the sales tax rate.
                        sales_tax_rate = subtotal * .06
                        #   Compute and print the total amount due.
                        total = sales_tax_rate + subtotal 

                        print(f"{name_product}: {product_quantity} @ {product_price}")
            print()
            print(f"Number of Items:  {number_items}")
            print(f"Subtotal: $ {subtotal:.2f}")
            print(f"Sales tax: {sales_tax_rate:.2f}")
            print(f"Total: {total:.2f}")
            print()
            print(f"Thank you for shopping at the {store_name}")
            print(f"{current_date_and_time:%a %b %d %I:%M:%S %x}\n")

    except FileNotFoundError as not_found_err:
        print(f"Error: unknown product ID in the request.csv file {not_found_err}")
        
    except PermissionError as perm_err:
        print(perm_err)
        
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)

def read_dictionary(products, KEY_COLUMN_INDEX):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    product_dict = {}   # creating a dictionary

    #   Open the products.csv file in VS Code and examine it.
    with open("2° semester - w05/products.csv") as product_file:
        #   read the products.csv file
        reader = csv.reader(product_file)
        #   Skipp the first line of the csv file
        next(reader)

        for products in reader: #The reader object returns each row as a list.
            
            if len(products) != 0:
                key = products[0]            
                product_dict[key] = products

    return product_dict


if __name__ == "__main__":
    main()