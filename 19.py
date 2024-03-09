# Project Euler project 19: Find the number of Sundays that fell on the first of
# the month during the 20th century (Jan 1 1901 - 31 Dec 2000)

# a leap year is any year divisible by 4, unless it is divisible by 100 and not 400
def leap(year):
    if (year % 100 == 0 and year % 400 != 0):
        return False
    elif (year % 4 == 0):
        return True
    else:
        return False

def monthLengths(year): 
    return [ 31, 29 if leap(year) else 28, 
        31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Days of the week, starting at Monday, as 1 Jan 1900 was a Monday, 
# which we take as our point of reckoning:
daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 
    'Thursday', 'Friday', 'Saturday', 'Sunday']

# calculate number of sundays that fell on the first of a month
daysSince1Jan1900 = 365
numSpecialSundays = 0
for year in range(1901, 2001):
    for month in range(0,12):
        for day in range(0, monthLengths(year)[month]):
            dayOfWeek = daysOfWeek[daysSince1Jan1900 % 7]
            if (dayOfWeek == 'Sunday' and day == 0):
                numSpecialSundays += 1
            daysSince1Jan1900 += 1

print(numSpecialSundays)