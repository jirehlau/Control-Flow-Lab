# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter jan and feb
#      Mar 20 - Jun 20: Spring april and may
#      Jun 21 - Sep 21: Summer july and august
#      Sep 22 - Dec 20: Fall october and november
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

months = input("Enter the month of the year (Jan - Dec)")
day_of_month = input("Enter the day of the month: ")

if month == "Jan" or month == "Feb":
    print("{month} {day_of_month} is Winter")

elif month == "Apr" or month == "May":
    print("{month} {day_of_month} is Spring") 

elif month == "Jul" or month == "Aug":
    print("{month} {day_of_month} is Summer") 

elif month == "Oct" or month == "Nov":
    print("{month} {day_of_month} is Fall") 

# SPECIFIED WINTER DATES 
elif month == "Dec" and day >= 21:
    print("{month} {day_of_month} is Winter")

elif month == "Mar" and day < 20:
    print("{month} {day_of_month} is Winter")

# SPECIFIED SPRING DATES 
elif month == "Mar" and day >= 20:
    print("{month} {day_of_month} is Spring")

elif month == "Jun" and day < 21:
    print("{month} {day_of_month} is Spring")

# SPECIFIED SUMMER DATES 
elif month == "Mar" and day >= 21:
    print("{month} {day_of_month} is Summer")

elif month == "Jun" and day < 22:
    print("{month} {day_of_month} is Summer")

# SPECIFIC FALL DATES 
elif month == "Sep" and day >= 22:  
    print("{month} {day_of_month} is Fall")

elif month == "Dec" and day < 21:
    print("{month} {day_of_month} is Fall")

else: 
    print("Invalid")