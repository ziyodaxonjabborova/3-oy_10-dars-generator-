import time

def fib():
    a,b=0,1
    while True:
        time.sleep(0.25)
        yield a
        a,b=b,a+b
        
        
for i in fib():
    print(i)
            
        
    
    
    
    
    
    