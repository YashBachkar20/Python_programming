#leap_year
#leap year divided byy 4

year = 2017

if (year % 400 == 0) and (year % 100 == 0) and (year % 4 ==0):
    print("This {0} this is leap year".format(year))

    
# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 100 != 0):
    print("{0} is a leap year".format(year))

else:
    print("This {0} this is not leap year".format(year))

