from weakref import WeakKeyDictionary
class Grade:

    def __init__(self):
        self._values = WeakKeyDictionary()
    
    def __get__(self, instance, instance_type):
        if instance is None:
            return self

        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if 0 <= value <= 100:
            self._values[instance] = value
        else:
            raise ValueError(f'Grade has to be between 0 and 100. Got {value}.')

class Exam:
    math_grade = Grade()
    writing_grade = Grade()
