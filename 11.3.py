def introspection_info(obj):
    info = {
        'type': type(obj).__name__, 'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': getattr(obj, '__module__', None)
    }
    return info

number_info = introspection_info(42)
print(number_info)

class Primer:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value

my_object = Primer(10)
object_info = introspection_info(my_object)
print(object_info)
