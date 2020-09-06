class Bosnian:
    """Bosnisn speaker"""

    def __init__(self):
        self.name = "Bosnian"

    def pozdravi_se(self):
        return "Vozdra. Sta ima ?"


class English:
    """British speaker"""

    def __init__(self):
        self.name = "British"

    def say_hallo(self):
        return "Hi, how are You?"


class Adapter():
    """changes generic name method named hi to individualised methods"""

    def __init__(self, object, **adapted_methods):
        """change the name of method"""
        self._object = object
        # add new dict item that establishes the mapping between the generic method name hi() and the concrete method
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self._object, attr)
