def log_args(func):
    def wrap(*args, **kwargs):
        with open("log.txt", "a") as f:
            f.write(f"Funksiya {func.__name__} chaqirildi\n")
            f.write(f"Args: {args}\n")
            f.write(f"Kwargs: {kwargs}\n\n")
        return func(*args, **kwargs)
    return wrap


@log_args
def salom_ber(name, yosh=None):
    print(f"Salom, {name}! Yoshingiz: {yosh}")


salom_ber("Ali", yosh=25)
salom_ber("Vali")
salom_ber("Hasan", yosh=30)
