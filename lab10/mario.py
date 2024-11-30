################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
################################################

from cs1graphics import *
from time import sleep

_scene = None
_world = None
score = 0

def create_world():
    global _scene, _world
    if _scene:
        raise RuntimeError("A world already exists!")
    _world = _World(500, 300)
    _scene = Canvas(_world.width, _world.height)
    _scene.setTitle("Mario World")
    _world.draw_scene()

class _World(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw_scene(self):
        global score
        # From my lab5 code:
        roof = Polygon(Point(105, 105), Point(175, 105), 
                       Point(170, 85), Point(110, 85)) 
        roof.setFillColor('darkgray') 
        roof.setDepth(30)

        # Drawable class has default depth of 50
        # Hierarchy: Square -> Rectangle -> Shape -> Drawable
        facade = Square(60, Point(140, 130))   
        facade.setFillColor('white')

        chimney = Rectangle(15, 28, Point(155, 85)) 
        chimney.setFillColor('red') 
        chimney.setBorderColor('red') 
        chimney.setDepth(20) # in front of roof 

        smoke = Path(Point(155, 70), Point(150, 65), 
                     Point(160, 55), Point(155, 50)) 
        smoke.setBorderWidth(2) 

        window = Rectangle(12, 24, Point(130, 120))
        window.setFillColor('black')
        window.setBorderColor('red')
        window.setDepth(40)

        ground = Rectangle(500, 150, Point(250, 225))
        ground.setFillColor('forestgreen')
        ground.setBorderColor('forestgreen')
        ground.setDepth(60)

        trees = [Polygon(Point(x, 85), Point(x-30, 160), Point(x+30, 160)) \
                 for x in [250, 350, 450]]

        world_components = [roof, facade, chimney, smoke, window, ground]
        for component in world_components: _scene.add(component)
        for tree in trees:
            tree.setFillColor('darkgreen')
            tree.setBorderColor('darkgreen')
            tree.setDepth(55)
            _scene.add(tree)

#define your own objects, e.g. Mario and Mushroom
class Mushroom(object):
    def __init__(self, x=200, y=92):
        self.mushroom = Layer()
        uppermush = Ellipse(38, 18, Point(x, y))
        uppermush.setFillColor('red')
        uppermush.setDepth(52)
        lowermush = Ellipse(35, 25, Point(x, y+8))
        lowermush.setFillColor('beige')
        lowermush.setDepth(53)
        self.mushroom.add(lowermush)
        self.mushroom.add(uppermush)
        self.mushroom.setDepth(52)

        self.layer = self.mushroom   # save mushroom shape in the class
        _scene.add(self.layer)  # add to global Canvas

class Mario (object):
    def __init__(self):
        self.layer = Layer()
        self.cx, self.cy = 60, 225
        
        hat = Rectangle(23, 7, Point(self.cx, self.cy-31))
        hat.setFillColor((238,28,37))
        hat.setBorderColor((238,28,37))
        hatshade = Rectangle(26, 2, Point(self.cx+10, self.cy-29))
        hatshade.setFillColor((238,28,37))
        hatshade.setBorderColor((238,28,37))
        head = Rectangle(20, 17, Point(self.cx, self.cy-20))
        head.setFillColor((251, 206, 177))
        head.setBorderColor((251, 206, 177))
        head.setDepth(53)
        self.eye = Circle(3.75, Point(self.cx+6.25+3.75, self.cy-20))
        self.eye.setFillColor('white')
        self.eye.setDepth(51)
        self.body = Rectangle(28, 40, Point(self.cx, self.cy+10))
        self.body.setFillColor((0,101,179))
        self.body.setBorderColor((0,101,179))
        self.body.setDepth(53)
        self.arm = Rectangle(14, 20, Point(self.cx-1.5, self.cy))
        self.arm.setFillColor((238,28,37))
        self.arm.setBorderColor((238,28,37))
        self.arm.setDepth(51)
        self.hand = Rectangle(10, 4, Point(self.cx-1.5, self.cy+12.5))
        self.hand.setFillColor('white')
        self.hand.setBorderColor('white')
        self.hand.setDepth(51)
        feet = [Rectangle(13, 7, Point(self.cx-8.5, self.cy+33.5)),
                Rectangle(13, 7, Point(self.cx+8.5, self.cy+33.5))]
        components = [hat, hatshade, head, self.eye, self.body, self.arm, self.hand]
        for component in components: self.layer.add(component)
        for foot in feet:
            foot.setFillColor((137,76,47))
            foot.setBorderColor((137,76,47))
            self.layer.add(foot)
        _scene.add(self.layer)
    
    def move(self, amt_x, amt_y):
        self.layer.move(amt_x, amt_y)
        self.cx += amt_x
        self.cy += amt_y
    
    #TODO: debug
    def attack(self):
        print(f"Arm position: {self.arm.getReferencePoint()}")
        print(f"Hand position: {self.hand.getReferencePoint()}")
        self.arm.adjustReference(self.cx-1.5, self.cy-7)
        #self.hand.adjustReference(self.cx-1.5, self.cy-7)
        self.arm.rotate(90)
        self.hand.rotate(90)
        print("Transformed!")
        print(f"Arm new position: {self.arm.getReferencePoint()}")
        print(f"Hand new position: {self.hand.getReferencePoint()}")
        sleep(0.5)
        self.arm.rotate(-90)
        self.arm.rotate(-90)

def update(val, mushroom):
    global score
    score += val
    score_display.setMessage(f"Score: {score}")
    _scene.remove(mushroom.layer)

def interact():
    global score, isMushAlive, mushrooms, transformed
    map_key = {'w': 1, 'b': -1, 'r': 2}

    while True:
        e = _scene.wait()
        if score == 30 and not transformed:
            mario.body.setFillColor('black')
            mario.body.setBorderColor('red')
            mario.eye.setFillColor('red')
            mario.body.scale(1.1)
            dagger = Rectangle(60, 5, Point(mario.cx+28.5, mario.cy+12.5))
            dagger.setFillColor('red')
            dagger.setBorderColor('red')
            dagger.setDepth(52)
            mario.layer.add(dagger) # TODO: dagger not appears
            _scene.remove(mario.layer)
            _scene.add(mario.layer)
            transformed = True
        
        d = e.getDescription()
        if d == 'keyboard':
            k = e.getKey()
            if k == "q":
                _scene.close()
                break
            elif k in ['w', 'b', 'r']: mario.move(20*map_key[k], 0)
            elif k == "j":
                mario.move(0, -40)
                sleep(0.3)
                mario.move(0, 40)
                for i, (alive, mush) in enumerate(zip(isMushAlive, mushrooms)):
                    # 19 is the half of the size of the ellipse of a mushroom
                    mario_in_range = abs(mario.cx - (150 + i * 100)) <= 19
                    if alive and mario_in_range:
                        update(20, mush) if i==3 else update(10, mush)
                        isMushAlive[i] = False
                        break
            elif k == "a": mario.attack()
            else: print(f"Wrong key input: {k}")

# Main routine
create_world()
score_display = Text(f"score: {score}", 20, Point(440, 25))
score_display.setFontColor('black')
_scene.add(score_display)
mushrooms = [Mushroom(pos_x, 243) for pos_x in [150, 250, 350, 450]]
isMushAlive = [True] * len(mushrooms)
transformed = False
mario = Mario()
interact()

# write your animation scenario here
# Greedy Mario travels around and attacks mushrooms, and whenever he kills a mushroom,
# Mario gains 10 points. Once Mario gains 30 points, he becomes devil mario,
# body color changing to orange and becoming larger. Once he becomes devil mario,
# he gains 20 points per mushroom.