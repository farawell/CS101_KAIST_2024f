################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
################################################

# Edmund Gunter 

import math

sin = math.sin
pi  = math.pi

def print_and_calc(n): 
    for i in range(int(n)):
        x = float(i) / 30.0 * 2 * pi
        print (sin(x))

def main():
    steps = input('How many steps? ')
    print_and_calc(steps)

main()
