import time

start_time = time.time()
i=0
while(i<5):
    i+=1
    time.sleep(1)
stopTime = time.time()
diff = stopTime - start_time    
print(diff)