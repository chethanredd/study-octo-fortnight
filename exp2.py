class date:
    def __init__(self, day, month, year):
        self.a = day
        self.m = month
        self.y = year
    def display(self):
        print("day:", self.a)
        print("month:", self.m)
        print("year:", self.y)
    def monthname(self):
        months = ["unknown", "january", "march", "April", "June", "July", "August", "September", "October", "November", "December" ]
        print("monthname", months[self.m])
    def isleapyear(self):
       if (self.y % 400 == 0) and (self.y %  100 ==0):
           print("It's a leap year")
       elif (self.y % 4 == 0) and (self.y % 100 != 0):
           print("Its a lea[ year")
       else:
           print("It's not a leap year")

d1=date(3, 8, 2000)
d1.display()
d1.monthname()
d1.isleapyear()