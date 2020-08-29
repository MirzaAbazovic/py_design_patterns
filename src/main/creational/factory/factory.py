class Dog:
    """Dog class """

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        return 'Av Av'


class Cat:
    """Cat class"""
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        return 'Mjau'


def get_pet(pet='dog'):
    """The factory method"""
    # we keep it in dic
    pets = dict(dog=Dog('Pas', 3), cat=Cat('Maca', 2))
    return pets[pet]
