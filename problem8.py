import time,random

def rand():
    while True:
        time.sleep(0.5)
        yield random.randint(1,100)
        
for i in rand():
    print(i)
        
        
        