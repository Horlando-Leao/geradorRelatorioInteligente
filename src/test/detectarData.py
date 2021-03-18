import re


def date_detector(text):
    date_pattern = re.compile('''
    ([12][0-9]|3[0-1]|0?[1-9])             # to detect days from 1 to 31
    ([./-])                                # to detect different separations
    (1[0-2]|0?[1-9])                       # to detect number of months
    ([./-])                                # to detect different seperations
    (2?1?[0-9][0-9][0-9])                  # to detect number of years from 1000-2999 years
     ''', re.VERBOSE)
    days = []
    months = []
    years = []
    dates = []
    for date in date_pattern.findall(text):
        days.append(int(date[0]))
        months.append(int(date[2]))
        years.append(int(date[4]))
    for num in range(len(days)):
    # appending dates in a list that dont need any filtering to detect wrong dates
        if months[num] not in (2, 4, 6, 9, 11):
            dates.append([days[num], months[num], years[num]])
    # detecting those dates with months that have only 30 days
        elif days[num] < 31 and months[num] in (4, 6, 9, 11):
            dates.append([days[num], months[num], years[num]])
    # filtering leap years with Feb months that have 29 days
        elif months[num] == 2 and days[num] == 29:
            if years[num] % 4 == 0:
                if years[num] % 100 == 0:
                    if years[num] % 400 == 0:
                        dates.append([days[num], months[num], years[num]])
                else:
                    dates.append([days[num], months[num], years[num]])
    # appending Feb dates that have less than 29 days
        elif months[num] == 2 and days[num] < 29:
            dates.append([days[num], months[num], years[num]])
    if len(dates) > 0:
        for date in dates:
            return (date)


""" data = '29.2.04'

date_detector(data) """


