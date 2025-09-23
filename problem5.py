import time

def square():
    n=1
    while True:
        time.sleep(0.25)
        yield n*n
        n+=1
        
for i in square():
    print(i)
        
    

    