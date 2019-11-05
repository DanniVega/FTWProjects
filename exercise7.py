# class Dog:

#     dog_info = "Hey dogs are cool!"

#     def bark(self):
#         print("BARK!")


class Car:

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        return(2019-self.year)


myCar = Car(2018,"SUV","toyota")
print(myCar)

