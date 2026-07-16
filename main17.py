class Build:
    __year = None   #encapsulation
    __city = None

    def __init__(self, year, city):   #
        self.year = year
        self.city = city

    def get_info(self):   #
        print("Year:", self.year, " City:", self.city, sep='')


class School(Build):
    __pupils = None

    def __init__(self, year, city,pupils=500):
        super(School, self).__init__(year, city)
        self.pupils = pupils

    def get_info(self):
        super().get_info()    #calls a method from the main class
        print("Pupils:", self.pupils)


class House(Build):
    pass


class Shop(Build):
    pass


school = School(1990, 'Seattle', 700)
#school.pupils = 500
school.get_info()
house = House(2010, 'New York')
house.get_info()
shop = Shop(2000, 'Miami')