# Write your code to expect a terminal of 80 characters wide and 24 rows high
# import gspraad library
import gspread
from google.oauth2.service_account import Credentials

#the program has access to the following scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Fresh-Cakes')

#access the data in purchase cell workseet
purchase = SHEET.worksheet('Purchase')

#pull all values from purchase worksheet
allData = purchase.get_all_values()


#accept user name
def enter_name():
    """
    accept user name
    """
    user_name = input("Enter your name here:\n")

    return user_name
     


def find_sales():
    """
    find sales  input from the user.
    """
    #while loop untill correct value is intered
    while True:
       print(f"Hello {enter_name()}Please enter sales data from the last market.")
       print("Data should be six numbers, separated by commas.")
       print("Example: 10,20,30,40,50,60\n")

       user_sale_data = input("Enter your data here:\n")

        #To get the broken up values as a list use split() method
       sale_data = user_sale_data.split(",")

       if validate_find_sales(sale_data):
           print("valid data")
           break
    return sale_data   


#to validate a sales data
def validate_find_sales(values):
    """
    change the string values to int and check if the values are 6 
    """


    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"6 values are required  you provided {len(values)}"
            )
    except ValueError as e:
        print(f"invalid data {e}, please try again.")
        return False
    
    return True

#update the worksheets
def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


def calculate_Remainder_data(Purchase_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating Remainder data...\n")
    stock = SHEET.worksheet("Stock").get_all_values()
    #pull stock value from worksheet
    stock_row = stock[-1]
    
    Remainder_data = []
    for stock, purchase in zip(stock_row, Purchase_row):
        Remainder = int(stock) - purchase
        Remainder_data.append(Remainder)
    return Remainder_data    

def get_last_5_entries_sales():
    """
    Collects columns of data from sales worksheet, collecting
    the last 5 entries for each sandwich and returns the data
    as a list of lists.
    """
    sales = SHEET.worksheet("Purchase")

    columns = []
    for ind in range(1, 7):
        #use col value method to access 1 column value
        column = sales.col_values(ind)
        columns.append(column[-5:])
    return columns    

def calculate_stock_data(data):
    """
    Calculate the average stock for each item type, adding 10%
    """
    print("Calculating stock data...\n")
    new_stock_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.1
        new_stock_data.append(round(stock_num))

    return new_stock_data


 #wrap the main function of the program with man function
def main():
    """
    Run all program func
    """
    #print(f"hello {enter_name()} you can calculate the needed stock value above")
    data = find_sales()
    purchase_data = [int(num) for num in data]
    update_worksheet(purchase_data, "Purchase")
    calculate_Remainder_data(purchase_data) 
    new_surplus_data= calculate_Remainder_data(purchase_data)
    update_worksheet(new_surplus_data, "Remainder")

    sales_columns = get_last_5_entries_sales()
    stock_data = calculate_stock_data(sales_columns)
    update_worksheet(stock_data, "Stock")

    

print("Welcome to Fresh-cakes cafe")
main()