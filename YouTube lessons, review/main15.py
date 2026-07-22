#OOP
class Dog:
    name = None
    age = None
    isHappy = None

    def set_data(self, dog_name, age, isHappy):
        self.name = dog_name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, "age:", self.age, "Happy:", self.isHappy )


dog1 = Dog()
dog1.set_data('Skubby', 3, True)

dog2 = Dog()
dog2.name = 'Bob'
dog2.age = 5
dog2.isHappy = False

dog1.get_data()
dog2.get_data()