
def extends(base_class):
    def decorator(func):
        setattr(base_class, func.__name__, func)
        return func
    return decorator

def module_not_imported(base_class, module):
    def decorator(func):
        def raise_error_on_call(*args, **kwargs):
            raise AttributeError("'" + base_class + "' object currently has no attribute '" + func.__name__ + "'. You can import it from module '" + module + "'")
        return raise_error_on_call
    return decorator
