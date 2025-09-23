import time

def multiple_of_five():
    
    for i in range(101):
        if i%5==0:
            time.sleep(1)
            yield i

        
for i in multiple_of_five():
    print(i)