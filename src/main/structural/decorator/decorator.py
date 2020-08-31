from functools import wraps

def to_upper(fun):
    """Defines the decorator and returns function"""

    # makes decorator transparent
    @wraps(fun)
    def decorator(param):
        """this is decorator to upper"""
        print("Decorating function {}, with parameter {}".format(fun.__name__, param))
        result = fun(param)
        return result.upper()

    return decorator


@to_upper
def echo(input_str):
    """original function"""
    return input_str
