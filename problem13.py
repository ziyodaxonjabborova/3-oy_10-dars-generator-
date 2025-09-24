import time


def timer(func):
    def wrap(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Funksiya {func.__name__} {(end-start)} soniya ishladi")
        return func(*args, **kwargs)
    return wrap


def log_args(func):
    def wrap(*args, **kwargs):
        with open("log.txt", "a") as f:
            f.write(f"Funksiya {func.__name__} chaqirildi\n")
            f.write(f"Args: {args}\n")
            f.write(f"Kwargs: {kwargs}\n\n")
        return func(*args, **kwargs)
    return wrap


@timer
@log_args
def salom_ber(name, yosh=None):
    print(f"Salom, {name}! Yoshingiz: {yosh}")
    time.sleep(2) 


salom_ber("Ali", yosh=25)

