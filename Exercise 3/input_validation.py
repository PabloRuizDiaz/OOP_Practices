import weakref
from numbers import Integral


### Part 1 ###

class IntegerValue:
    def __init__(self, min_value, max_value):
        self.values = {}
        self._min_value = min_value
        self._max_value = max_value
        
    def __set__(self, instance, value):
        if not isinstance(value, Integral):
            raise ValueError(f'{value} must be an integer.')

        if self._min_value > value:
            raise ValueError(f'{self._min_value} is higher than {value}, value should be more than minimum number.')
        
        if self._max_value < value:
            raise ValueError(f'{self._max_value} is lower than {value}, value should be less than maximum number.')

        self.values[id(instance)] = (weakref.ref(instance, self._remove_object), int(value))
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(id(instance))[1]
        
    def _remove_object(self, weak_ref):
        reverse_lookup = [key for key, value in self.values.items() if value[0] is weak_ref]
        
        if reverse_lookup:
            key = reverse_lookup[0]
            del self.values[key]


class CharField:
    def __init__(self, min_value=0, max_value=255):
        self.values = {}
        self._min_value = min_value
        self._max_value = max_value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{value} must be a string.')

        if self._min_value > len(value):
            raise ValueError(f'{self._min_value} is higher than {value}, string should be more than minimum characters.')

        if self._max_value < len(value):
            raise ValueError(f'{self._max_value} is lower than {value}, string should be less than maximum characters.')

        self.values[id(instance)] = (weakref.ref(instance, self._remove_object), str(value))

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(id(instance))[1]

    def _remove_object(self, weak_ref):
        reverse_lookup = [key for key,
                          value in self.values.items() if value[0] is weak_ref]

        if reverse_lookup:
            key = reverse_lookup[0]
            del self.values[key]

# class Person:
#     name = CharField(0, 15)
#     age = IntegerValue(0, 100)


# test = Person()
# test.name = 'Alex'
# test.age = 20

# print(f'{test.name} and {test.age}')


### Part 2 ###

class BaseValidator:
    def __init__(self, type_):
        self.values = {}
        self._type = type_

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise ValueError(f'{value} must be {self._type}.')

        self.values[id(instance)] = (weakref.ref(instance, self._remove_object), str(value))

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(id(instance))[1]

    def _remove_object(self, weak_ref):
        reverse_lookup = [key for key,value in self.values.items() if value[0] is weak_ref]

        if reverse_lookup:
            key = reverse_lookup[0]
            del self.values[key]


# class Person:
#     name = BaseValidator(str)
#     age = BaseValidator(Integral)


# test = Person()
# test.name = 'Alex'
# test.age = 20

# print(f'{test.name} and {test.age}')
