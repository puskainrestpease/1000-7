# -*- coding: utf-8 -*-
try:
    import random
    import time
    from termcolor import cprint
except ModuleNotFoundError or ImportError as e:
    exit(f'{e}\nCheck out imports!')

# x = will be 1000 - 7 we force python print to subtract from 1000 - 7.
# We set the time for sleep (so that our project does not immediately show a complete solution)
# TODO: for example, as in my case it will be 0.1ms
# x will have a value of - 7

x = 1000 - 7
mixcolors = random.choice(['green', 'red', 'yellow', 'blue', 'white', 'grey'])

if __name__ == '__main__':
    while x > 7:
        cprint(f'🧛 {x} - 7 = {x - 7}', f'{mixcolors}')
        x -= 7
        time.sleep(0.1)
