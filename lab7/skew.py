from math import *
from cs1media import *

img = load_picture( "aespa.png" )
w,h = img.size()

#----------------------------------------------------------#
#
# Function skew
#
# Input:
#		img: loaded image
#		direction: vertical or horizontal
#		angle: -89 to 89 degrees
#
# Output:
#		new_img: skewed image
#		print “Wrong input!!!” if inputs are not in range
#
#----------------------------------------------------------#

def skew(img, direction, angle):
    #implement here
    #new_img = create_picture(new_w, new_h)

    # Input integrity check
    correct_direction = direction in ['vertical', 'horizontal']
    angle_in_range = (-89 < angle < 89)
    proper_input = all([correct_direction, angle_in_range])
    if not proper_input: 
        print("Wrong input!!!")
        return
    
    # Initialization
    w, h = img.size()
    tan_angle = tan(radians(abs(angle)))

    if direction == 'vertical':
        # Dynamic image size transformation
        _w = int(h * tan_angle + w) + 1
        new_img = create_picture(_w, h)

        for y in range(h):
            for x in range(w):
                pixel = img.get(x, y)
                new_x = int(x + (h - y) * tan_angle)
                if angle < 0: 
                    new_x = int(x + y * tan_angle)
                new_img.set(new_x, y, pixel)
    else:
        _h = int(w * tan_angle + h) + 1
        new_img = create_picture(w, _h)

        for x in range(w):
            for y in range(h):
                pixel = img.get(x, y)
                new_y = int(y + (w - x) * tan_angle)
                if angle < 0:
                    new_y = y + x * tan_angle
                new_img.set(x, new_y, pixel)
    
    new_img.show()
    return

# skew(img, 'vertical', 123)
# skew(img, 'what', 20)
skew(img, "vertical", 88)
# skew(img, "horizontal", 88)

