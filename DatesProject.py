"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """

    next_year = []
    next_month = []

    # deals with comparing one month to the next when spanning
    # different years

    if month == 12:
        next_year = year + 1
        next_month = 1
    else:
        next_month = month + 1
        next_year = year

    begin_month = datetime.date(year, month, 1)
    end_month = datetime.date(next_year, next_month, 1)
    delta = end_month - begin_month

    return delta.days

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    # checks that the date is valid. Returns false if invalid

    if year < 1 or year > 9999:
        print("Enter valid year")
        return False
    elif month < 1 or month > 12:
        print("Enter a valid month")
        return False
    elif day < 1 or day > days_in_month(year, month):
        print("Enter a valid day")
        return False
    else:
        return True


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """

    # check that date is valid
    check1 = is_valid_date(year1, month1, day1)
    check2 = is_valid_date(year2, month2, day2)

    # if the dates aren't valid returns the reason
    # and exits the function

    if not(check1) or not(check2):
        print("Please Enter a Valid Date")
        return 0

    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)

    # checks that the second date is after the first
    if date2 < date1:
        print("Second Day Must Come After First")
        return 0

    delta = date2 - date1
    return delta.days


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """

    check1 = is_valid_date(year, month, day)
    if not(check1):
        return 0

    now = datetime.date.today()

    year1 = year
    month1 = month
    day1 = day

    year2 = now.year
    month2 = now.month
    day2 = now.day

    age = days_between(year1, month1, day1, year2, month2, day2)

    if age == 0:
        return 0
    return age