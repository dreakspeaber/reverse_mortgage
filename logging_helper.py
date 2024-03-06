from functools import wraps

def log_method(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # Print class name, function name, and its arguments
        print(f"Calling: {self.__class__.__name__}.{func.__name__}")
        print(f"Input Arguments: {args} {kwargs}")
        # Execute the function
        result = func(self, *args, **kwargs)
        # Print the result
        print(f"Result : {result}")
        return result
    return wrapper
