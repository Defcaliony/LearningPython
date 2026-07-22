class Dog:
    name = None
    age = None
    isHappy = None

    def __init__(self, name='Bob', age=1, isHappy=True): #constructor
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, dog_name, age = 1, isHappy = True):
        self.name = dog_name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, "age:", self.age, "Happy:", self.isHappy )


dog1 = Dog(age=5)
#dog1.set_data('Skubby', 3, True)
#dog1.set_data('Alex')
dog2 = Dog('Bob', 5, False)
#dog2.name = 'Bob'
#dog2.age = 5
#dog2.isHappy = False

#dog1.get_data()
#dog2.get_data()