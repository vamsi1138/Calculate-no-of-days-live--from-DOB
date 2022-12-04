class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y
monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def countLeapYears(d):
    years = d.y
    if (d.m <= 2):
        years -= 1
    return int(years / 4) - int(years / 100) + int(years / 400)

def getDifference(dt1, dt2):
    n1 = dt1.y * 365 + dt1.d
    for i in range(0, dt1.m - 1):
        n1 += monthdays[i]
    n1 +=countLeapYears(dt1)

    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 +=monthdays[i]
    n2 += countLeapYears(dt2)

    return(n2 - n1)
day=int(input("Enter a day in your DOB:"))
month=int(input("Enter a month in your DOB:"))
year=int(input("Enter a year in your DOB:"))
dt1 = Date(day,month,year)
dt2 = Date(28, 11, 2022)
print(getDifference(dt1, dt2), "days")
