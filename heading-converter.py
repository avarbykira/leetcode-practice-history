from datetime import date


HEADING = "1637. Widest Vertical Area Between Two Points Containing No Points"

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