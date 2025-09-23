import time

def natural(l):
    for i in l:
        if isinstance(i,int) and i>0:
            time.sleep(0.25)
            yield sum([int(j) for j in str(i)])
            
            

    
    
l=[18,21,-9,2.4,30]
    
for i in natural(l):
    print(i)