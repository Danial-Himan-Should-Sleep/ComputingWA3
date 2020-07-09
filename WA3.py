# ©DANIAL & HIMAN 2020. Any attempts to distribute this and we will personally snitch on you.
# We took a long time to do this. Learning and understanding the code is perfectly fine, but stealing and copy pasting it is not the same as learning.
# made by danial and himan. now let us sleep pls. dont ask what anything does. learn it yourself.

# - Input of 3 charity names.
# - The names to be printed out with the index in front of them.
# - A choice from 1-3 to be chosen and to be submitted.
# - Input of customers "receipt", must be more than 0 dollars and be in dollars.
# - The donation of money from the customer; 1% of total bill.
# - Print out the name of the charity with the amount donated.

## Variables
CHARITIES = [] #
HAS_GIVEN_CHOICE = False # Boolean. Turns to true once customer has given their CHARITY preference in the correct format. Remains false if incorrect. 
CUSTOMER_CHOICE = 0 # Integer. This is the index (position) in the CHARITIES List. 
HAS_GIVEN_BILL = False # Boolean. Turns to true once customer has inputted their bill amount correctly. Remains false if incorrect. 
CUSTOMER_BILL = 0 # Integer. This is used to store the customers bill after it has been inputted.
CHARITIES_SUBMITTED = 0 # Interger. This is just to keep track of the amount of charities someone has inputted. Once it reaches 3, it stops adding to this.

# FUNCTION calculatePercentage(int percent, int int). Returns an integer; Returns a percentage of value given.   
def calculatePercentage(percent, int): 
  int = int / 100
  int = int * percent
  return int

# Task 1A
while (CHARITIES_SUBMITTED < 3): # Continues to loop until 3 charities have been inputted                          
  charityName = input("Input the name of the charity.") # Quite obvious on what it does.
  CHARITIES_SUBMITTED+=1 # It's basically CHARITIES_SUBMITTED = CHARITIES_SUBMITTED + 1 but shorter. 
  CHARITIES.append(charityName) # .appends is basically a function to add something to a list. In this case, .appends adds the charity name to the CHARITIES list. 

# Task 1B
for x in range(3): 
  print("{0} | {1}".format(x+1, CHARITIES[x])) # Prints out all the charities with its number.

# Task 1C
while (HAS_GIVEN_CHOICE == False):
  choice = int(input("Input a charity you would like to donate to. Pick from 1-3\n")) # Pretty obvious in what it does.
  if (choice > 0) and (choice < 3): # This validates to make sure user is only submitting a integer from 1-3 as there are only 3 charities.
    HAS_GIVEN_CHOICE = True # Sets this to true so while loops stop.
    CUSTOMER_CHOICE = choice - 1 # Because of how list works in python, the first item in the list is referenced to 0. 
  else:
    print("\n\nPlease pick a number from 1-3! Try Again!") # If the charity given by the user is more than 3 or less than 0, it tells the user to input again.
 
 # Task 1D
while (HAS_GIVEN_BILL == False):
  bill = int(input("Please input your bill in dollars! $")) # Pretty obvious here.
  if (bill < 0): # If user inputs a bill of less than $0, it ask the user to redo.
    print("\n\nThe bill needs to be more than $0. Please try again.")
  else:
    HAS_GIVEN_BILL = True # Same like the reasoning above.
    CUSTOMER_BILL = bill # Sets the bill of customer to what they inputted.

# Task 1F
print("{0} | ${1}".format(CHARITIES[CUSTOMER_CHOICE], calculatePercentage(1, CUSTOMER_BILL))) # This outputs the charity the person has selected and the donation they have given.
