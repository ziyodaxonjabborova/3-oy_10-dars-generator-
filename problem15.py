import datetime

def only_monday(func):
    def wrap(*args, **kwargs):
        today = datetime.datetime.today().weekday()  
        if today == 0:
            return func(*args, **kwargs)
        else:
            print("Bugun dushanba emas, funksiya ishlamaydi!")
    return wrap

@only_monday
def salom_ber(name):
    print(f"Salom, {name}!")

salom_ber("Ali")
