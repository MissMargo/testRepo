class Car(object):
    def __init__(self, model, colour, engine_volume):
        self.model = model
        self.colour = colour
        self.engine_volume = engine_volume

    def get_model(self):
        return self.model

    def get_colour(self):
        return self.colour

    def get_engine_volume(self):
        return self.engine_volume

    def moveforward(self):
        pass

    def movebackward(self):
        pass


class CarOne(Car):
    def moveforward(self):
        print("go forward")

    def movebackward(self):
        print("go backward")


class CarTwo(CarOne):
    def moveright(self):
        print("move right")

    def moveleft(self):
        print("move left")


Audi = CarOne('A4', 'Red', '2')
print(Audi.model)
Audi.moveforward()
Audi.movebackward()
BMW = CarTwo("X7", "Black", "2.5")
print(BMW.model)
BMW.moveforward()
BMW.movebackward()
BMW.moveright()
BMW.moveleft()
