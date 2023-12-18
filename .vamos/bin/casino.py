"""
casino: simple Python script to print random numbers 0 <= n <= 36
"""

import numpy as np
import sys

def random():
    red = [32,4,2,17,6,13,11,8,10,24,33,20,31,22,29,28,35,26]
    number = np.random.randint(37)

    if number == 0:
        print("\x1b[32mgreen:",number,"\x1b[0m")
    elif number in red:
        print("\x1b[31mred:",number,"\x1b[0m")
    else:
        print("black:",number)

def main():
    if len(sys.argv) <= 1:
        random()
    elif sys.argv[1] == '-?' or sys.argv[1] == '--help':
        print('usage: casino         # get random number (0 <= n <= 36)')
        print('       casino <n>     # n times get random number')
        print('       casino -?      # show help')
        print('       casino --help  # show help')
    else:
        try:
            n = int(sys.argv[1])
        except:
            n = -1

        if (n <= 0):
            print('bad input (=> casino -?)')
        else:
            for i in range(n):
                random()

if __name__ == '__main__':
    main()
