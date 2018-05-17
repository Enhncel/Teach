def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False



def dayInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 \
       or month == 8 or month == 10 or month == 12:
       return 31
    else:
       if month == 2 :
           if isLeapYear(year):
                return 29
           else:
                return 29
       return 30


def nextDay(year, month, day):
    if day < dayInMonth(year, month):
        return year, month, day+1
    else:
        if month < 12:
            return year, month+1,1
        else:
            return year+1,1,1



def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1,  month1, day1 = nextDay(year1, month1, day1)
        days = days + 1
    return days

def test():
     print daysBetweenDates(1918, 3, 7, 2018, 3, 7)

test()
