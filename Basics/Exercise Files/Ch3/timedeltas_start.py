#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it


# print today's date


# print today's date one year from now


# create a timedelta that uses more than one argument


# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks = 1)
print("1 week ago it was: ", t)

### How many days until April Fools' Day?
today =  date.today()
afd = date(today.year, 4, 1)
if afd < today:
    print("April fools day has gone by %d" % ((today-afd).days))
    afd = afd.replace(year=today.year+1)
else:
    print("April fools day has not gone")
    # afd = afd.replace(year=today.year+1)

    time_to_afd = afd - today
    print("next april fool will come in ", time_to_afd, "days")

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# Now calculate the amount of time until April Fool's Day  

