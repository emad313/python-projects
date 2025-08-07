import time
from functools import wraps

def log_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        if hasattr(result, '__iter__') and not isinstance(result, str):
            def generator_wrapper():
                nonlocal start_time
                for item in result:
                    yield item
                end = time.time()
                print(f"Performance: {func.__name__} took {end - start_time:.4f} seconds")
            return generator_wrapper()
        else:
            end = time.time()
            print(f"Performance: {func.__name__} took {end - start_time:.4f} seconds")
            return result
    return wrapper