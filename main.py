import copy

class Prototype:
    """ A prototype Case Class """

    def deep_clone(self):
        """ Return a clone of the instance (self reference the instance itself) """
        return copy.deepcopy(self)

    def shallow_clone(self):
        """ Returns a shallow copy of the instance """
        return copy.copy(self)


class Cheese(Prototype):
    """ A Cheese class """

    def __init__(self, name=None):
        """ Constructor """
        self._name = name
        self._properties = {}

    def get_properties(self):
        return self._properties

    def get_property(self, key):
        return self._properties.get(key, None)

    def set_property(self, **kwargs):
        self._properties.update(**kwargs)

    def delete_property(self, key):
        del self._properties[key]

gouda = Cheese("Gouda")
gouda.set_property(color='yellow', texture='soft')
deep_clone_gouda = gouda.deep_clone()
shallow_clone_gouda = gouda.shallow_clone()

gouda.set_property(nationality='Dutch')
print(gouda.get_properties())
print(shallow_clone_gouda.get_properties())
print(deep_clone_gouda.get_properties())
