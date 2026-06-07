n = int(input("Enter a number to chalculate table:"))
r = 1
print("Here is the table of ",n)
while(r<=10):
    print(r*n)
    r+=1
print()
#coundown timer
import time 
timer = 3
while timer>0:
    print(timer)
    time.sleep(1)
    timer-=1
print("Happy birthday")