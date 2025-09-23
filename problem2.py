import time

def word(text:str):
    for i in text.split():
        time.sleep(1)
        yield i
        
for i in word(input("Matn kiriting: ")):
    print(i)
    