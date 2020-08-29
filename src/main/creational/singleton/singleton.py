class Borg:
    """Class making attribute global"""
    _shared_state = {} # Attribute dic

    def __init__(self):
        self.__dict__ = self._shared_state # make it attibute dic

class Singleton(Borg):
    """This class shares all its atributes among all instances"""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # update the atribute dic by instering key-value pairs
        self._shared_state.update(kwargs)

    def __str__(self):
        return (self._shared_state)
