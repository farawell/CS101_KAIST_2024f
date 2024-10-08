################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
################################################

# Edmund Gunter 2

import math

sin = math.sin
pi  = math.pi

for i in range(41) :
    x = float(i) / 40.0 * 2 * pi
    character_count_per_line = 40 + 40*sin(x)
    
    output_str = '#' * int(character_count_per_line)
    print (output_str)
