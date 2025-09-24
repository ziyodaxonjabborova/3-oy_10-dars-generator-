def count_calls(func):
    count = 0  

    def wrap(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Funksiya {count}-marta chaqirildi")
        return func(*args, **kwargs)

    return wrap


@count_calls
def salom_ber(name):
    print(f"Salom, {name}!")


salom_ber("Ali")
salom_ber(name="Vali")
salom_ber("Hasan")
