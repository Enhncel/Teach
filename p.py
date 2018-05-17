# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet!
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                 leap = 1
            else:
                 leap = -1
        else:
             leap = -1
    else:
         leap = -1
    return leap

    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    head = 0
    end = 0
    if isLeapYear(y1) == -1:
        while m1 <= 12:
            head = head + daysOfMonths[m1-1]-d1
            m1= m1 + 1
        #head = daysOfMonths[0]+daysOfMonths[1]+1+daysOfMonths[2]+daysOfMonths[3]+daysOfMonths[4]+d1
    else:
        while m1 <= 12:
            if m1 <=2 and d1 <29:
                head = head + daysOfMonths[m1-1]-d1+1
            else:
                head = head + daysOfMonths[m1-1]-d1
            m1= m1 + 1
        #head = daysOfMonths[0]+daysOfMonths[1]+daysOfMonths[2]+daysOfMonths[3]+daysOfMonths[4]+d1
    if isLeapYear(y2) == -1:
        if  m2 == 1:
            end = d2
        else:
            while m2 >= 2 and m2 <= 12 :
                end = end + daysOfMonths[m2-2]+d2
                m2 = m2 - 1
    else:
        if  m2 <= 2 :
            end = daysOfMonths[0]+d2

        else:
            while m2 >2 and m2 <= 12 :
                end = end + daysOfMonths[m2-2]+d2+1
                m2 = m2 - 1

        #head = daysOfMonths[0]+daysOfMonths[1]+1+daysOfMonths[2]+daysOfMonths[3]+daysOfMonths[4]+d1
    dayall = 0
    while y1 < y2:
        if isLeapYear(y1+1) == -1:
            y=365
        else:
            y=366
        day = y
        y1 = y1+1
        dayall=dayall+day
    #if isLeapYear(y1) == -1:
        ##headdy = daysOfMonths[0]+daysOfMonths[1]+1+daysOfMonths[2]+daysOfMonths[3]+daysOfMonths[4]+d1
    #else:
        #headdy  = daysOfMonths[0]+daysOfMonths[1]+daysOfMonths[2]+daysOfMonths[3]+daysOfMonths[4]+d1
    ##endday = daysOfMonths[2]+daysOfMonths[3]+daysOfMonths[4]+daysOfMonths[5]+daysOfMonths[6]+daysOfMonths[7]+daysOfMonths[8]+daysOfMonths[9]+daysOfMonths[10]+daysOfMonths[11]-d2
    return dayall-head-end
    #return dayall
    #return endday
    #return headdy

print daysBetweenDates(1912, 12, 12, 2012, 12, 12)
