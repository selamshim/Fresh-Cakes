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

print(allData)

def find_sales():
    """
    find sales  input from the user.
    """
    #while loop untill correct value is intered
    while True:
       print("Please enter sales data from the last market.")
       print("Data should be six numbers, separated by commas.")
       print("Example: 10,20,30,40,50,60\n")

       user_sale_data = input("Enter your data here: ")

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
    print(values)

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

#to update te purchase worksheet
def update_purchase_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """

    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("Purchase")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")

data = find_sales()
purchase_data = [int(num) for num in data]
update_purchase_worksheet(purchase_data) 