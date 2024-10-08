################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
################################################

# Edmund Gunter 3

import math

sin = math.sin
pi  = math.pi

for i in range(41) :
    x = float(i) / 40.0 * 2 * pi
    character_count_per_line = 40 + 40*sin(x) # Change this line to print out sine curve correctly.
    num = int(character_count_per_line)
    
    for _ in range(num - 1):
        print(' ', end='')
    print('#')
