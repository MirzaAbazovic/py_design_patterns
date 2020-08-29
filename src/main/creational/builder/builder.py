class Car():
    """Object """

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.engine, self.tires)


class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_engine()
        self._builder.add_tires()
        return self._builder.car;


class Builder:
    """Abstract builder"""

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()

    def add_model(self): pass

    def add_engine(self): pass

    def add_tires(self): pass


class ToyotaBuilder(Builder):
    """Concrete builder """

    def add_model(self):
        self.car.model = 'Toyota'
        return self.car

    def add_engine(self):
        self.car.engine = 'Diesel'
        return self.car

    def add_tires(self):
        self.car.tires = 'Good Year'
        return self.car
