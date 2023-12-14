from datetime import date


HEADING = "2482. Difference Between Ones and Zeros in Row and Column"

# delete all spaces in it
HEADING = HEADING.replace(" ", "-")

# lowercase all letters
# HEADING = HEADING.lower()

# remove all special characters
HEADING = HEADING.replace(".", "")
HEADING = HEADING.replace("(", "")
HEADING = HEADING.replace(")", "")
HEADING = HEADING.replace("%", "")

# add today's date at the end of the string
HEADING = HEADING + "-" + date.today().strftime("%b-%d-%Y")

# print the result
print(HEADING)