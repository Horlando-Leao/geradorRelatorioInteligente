import re

def date_is_valid(day: int, month: int, year: int) -> bool:
    return (month not in (2, 4, 6, 9, 11)   # 31 days in month (Jan, Mar, May, Jul, Aug, Oct, Dec).
    or day < 31 and month in (4, 6, 9, 11)  # 30 days in month (Feb, Apr, Jun, Sep, Nov).
    or month == 2 and day == 29 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
                                            # February, 29th in a Gregorian leap year.
    or month == 2 and day < 29)             # February, 1st-28th.

def date_detector(text: str):
    date_pattern = re.compile('''
    (?P<day>[12][0-9]|3[0-1]|0?[1-9])   # to detect days from 1 to 31
    (?P<sep>[./-])                      # to detect different separations
    (?P<month>1[0-2]|0?[1-9])           # to detect number of months
    (?P=sep)                            # to detect different seperations
    (?P<year>2?1?[0-9][0-9][0-9])       # to detect number of years from 1000-2999 years
     ''', re.VERBOSE)

    dates = []
    for match in date_pattern.finditer(text):
        date = match.groupdict()                            # convert Match object to dictionary.
        del date['sep']                                     # we don't need the separator any more.
        date = {key: int(val) for key, val in date.items()} # apply int() to all items.
        
        if date_is_valid(date['day'], date['month'], date['year']):
            dates.append(date)

    if len(dates) > 0:
        for date in dates:
            print(date)

data = '30-06-2012, 31-12.2012'

date_detector(data)