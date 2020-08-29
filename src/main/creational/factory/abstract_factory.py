class Dog:
    """Dog class """

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        return 'Av Av'

    def __str__(self):
        return 'Dog'


class Cat:
    """Cat class"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        return 'Mjau'

    def __str__(self):
        return 'Cat'


class DogFactory:
    """Concrete factory """

    def get_pet(self):
        """Returns dog object"""
        return Dog('Laki', 2)

    def get_food(self):
        """Returns dogs food object"""
        return 'Dog food'

class CatFactory:
    """Concrete factory """

    def get_pet(self):
        """Returns dog object"""
        return Cat('Micika', 3)

    def get_food(self):
        """Returns dogs food object"""
        return 'Cat food'


class PetStore:

    def __init__(self, pet_factory=None):
        """pet_factory is Abstract factory"""
        self._pet_factory = pet_factory

    def get_pet(self):
        return self._pet_factory.get_pet()

    def get_pet_food(self):
        return self._pet_factory.get_food()

    def show_pet(self):
        """Utility to display details of returned object by concrete factory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        print("Our pet is '{}'".format(pet))
        print("Our pet says '{}'".format(pet.speak()))
        print("Our pet eats '{}'".format(pet_food))
