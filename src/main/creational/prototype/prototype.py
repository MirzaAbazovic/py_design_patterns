import copy


class Prototype:
    def __init__(self):
        """dic object will be containing object that will be cloned """
        self._objects = {}

    def register_object(self, name, obj):
        """register object"""
        self._objects[name] = obj;

    def unregister_object(self, name):
        """unregister object"""
        del self._objects[name]

    def clone(self, name, **attr):
        # *args and *kwargs are special keyword which allows function to take variable length argument.
        # **kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed.
        """clone registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.name = "Toyota"
        self.color = "Gray"
        self.options = "Ex"

    def __str__(self):
        return '{} {} {}'.format(self.name, self.color, self.options)
