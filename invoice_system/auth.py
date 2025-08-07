from functools import wraps

AUTH_TOKEN = "secret123"

def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = input("Enter authentication token: ")
        if token == AUTH_TOKEN:
            return func(*args, **kwargs)
        else:
            print("Authentication failed. Access denied.")
            return None
    return wrapper