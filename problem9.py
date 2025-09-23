import datetime,time

def second():
    while True:
        time.sleep(1)
        yield datetime.datetime.now().second
        
for i in second():
    print(i)
        
        
        