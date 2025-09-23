import time

unli=["a","e","o","u","o'","i"]

def vowel(text:str):
    for i in text:
        if i in unli:
            time.sleep(1)
            yield i

        
for i in vowel(input("Matn kiriting: ")):
    print(i)
    