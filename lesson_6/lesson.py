def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(n):
                func(*args,**kwargs)
            return wrapper
        return decorator
    
    
@repeat(4)   
def grear(name):
    print(f"Hello, {name}?")

print(grear)