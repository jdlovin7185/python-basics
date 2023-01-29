import time
import datetime

# this will give you the current GM time
# GMT is Greenwich Mean Time
print(time.gmtime())
# this will give you a time structure containing 9 values

print("To get the local time\n", time.localtime())
# this will give you the same structure of time as it did for gmtime()

print("you can get todays date extracted in a string format")
print("Todays date using the time module \n", time.strftime("%m-%d-%Y"))
# the string
print("==========================")
print("datetime module begins here")

# this will give you today's date without having to actually format it Y-M-D
print("Today's date with the datetime module\n", datetime.date.today())

# if you want to get it printed out in a specified string format
print("Today's date (dd/mm/yyyy using the date time module \n", datetime.date.today().strftime("%d/%m/%Y"))

print(datetime.datetime.strptime("23/29/01", "%y/%d/%m"))
