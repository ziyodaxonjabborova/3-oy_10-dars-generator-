import time

def unique(l:list):
    for i in l:
        if l.count(i)==1:
            time.sleep(0.25)
            yield i
            
l=["salom","ali","hello","vali","salom","hello"]

for i in unique(l):
    print(i)
            
