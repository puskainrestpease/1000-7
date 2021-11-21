import time

# x will be 1000 - 7 we force python print to subtract from 1000 - 7. We set the time for sleep (so that our project does not immediately show a complete solution), for example, as in my case it will be 0.1ms

x = 1000 - 7

while x > 7:
    print(f"{x} - 7 = {x-7}")
    x -=7
    time.sleep(0.1)

# x will have a value of - 7