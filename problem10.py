def to_string(func):
    def wrap(*args,**kvargs):
        return str(func(*args,**kvargs))
    return wrap
    


@to_string
def add(a,b):
    return a+b

print(type(add(1,2)))  # string chiqdi


