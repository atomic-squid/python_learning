# from LAB: https://edube.org/learn/pe-2/lab-the-calendar-module-1

"""
During this course, we looked at the `Calendar` class a bit. Your task is to extend its functionality
with a new method called `count_weekday_in_year`, which takes a year and a weekday as parameters, and
then returns the number of occurrences of a specific weekday in the year.

Use the following tips:

* Create a class called `MyCalendar` that extends the Calendar class;
* create the `count_weekday_in_year` method with the year and weekday parameters. The weekday parameter
  should be a value between 0-6, where 0 is Monday and 6 is Sunday. The method should return the number
  of days as an integer;
* in your implementation, use the `monthdays2calendar` method of the Calendar class.

The following are the expected results:

Sample arguments

`year=2019, weekday=0`

Expected output

`52`

Sample arguments

`year=2000, weekday=6`

Expected output

`53`
"""

from calendar import Calendar

class MyCalendar(Calendar):
    def count_weekday_in_year(self, year, weekday):
        count_of_days = 0
        for month in range(1,13):
            for week in self.monthdays2calendar(year, month):
                for day, day_of_week in week:
                    if day != 0 and day_of_week == weekday:
                        count_of_days += 1
        return count_of_days


c = MyCalendar()

print(c.count_weekday_in_year(2019, 0))
print(c.count_weekday_in_year(2000, 6))
print(c.count_weekday_in_year(2024, 2))