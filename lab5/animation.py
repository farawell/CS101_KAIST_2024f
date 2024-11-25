################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
################################################

from cs1graphics import *
from time import sleep

def draw_animal():
    # Implement this function.
    global paper 
    paper = Canvas(300, 200, 'skyBlue', 'My World')

    roof = Polygon(Point(105, 105), 
                   Point(175, 105), 
                   Point(170, 85), 
                   Point(110, 85)) 
    roof.setFillColor('darkgray') 
    roof.setDepth(30) # in front of façade 
    paper.add(roof)

    facade = Square(60, Point(140, 130))   
    facade.setFillColor('white')
    paper.add(facade)

    chimney = Rectangle(15, 28, Point(155, 85)) 
    chimney.setFillColor('red') 
    chimney.setBorderColor('red') 
    chimney.setDepth(20) # in front of roof 
    paper.add(chimney)

    smoke = Path(Point(155, 70), 
                 Point(150, 65), 
                 Point(160, 55), 
                 Point(155, 50)) 
    smoke.setBorderWidth(2) 
    paper.add(smoke) 

    window = Rectangle(12, 24, Point(130, 120))
    window.setFillColor('black')
    window.setBorderColor('red')
    window.setDepth(40)
    paper.add(window)

    ground = Rectangle(300, 80, Point(150, 160))
    ground.setFillColor('green')
    ground.setBorderColor('green')
    ground.setDepth(51)
    paper.add(ground)

    tire1 = Circle(10, Point(15, 175)) 
    tire1.setFillColor('black') 
    car.add(tire1)

    tire2 = Circle(10, Point(55, 175)) 
    tire2.setFillColor('black') 
    car.add(tire2)

    body = Rectangle(70, 30, Point(35, 160)) 
    body.setFillColor('blue') 
    body.setDepth(60) # behind the tires 
    car.add(body)

    car_roof = Rectangle(35, 15, Point(48, 137.5))
    car_roof.setFillColor('brown')
    body.setDepth(60)
    car.add(car_roof)

    car.setDepth(20) # in front of the house
    paper.add(car)

    gun_body = Rectangle(70, 8, Point(95.5, 137.5))
    gun_body.setFillColor('brown')
    gun_body.setDepth(10)
    gun.add(gun_body)
    paper.add(gun)

def show_animation():
    delay = 1

    for _ in range(10):
        sleep(delay)
        car.move(30, 0)
        gun.move(35, 0)
        sleep(delay)
        gun.move(-5, 0)

car = Layer()
gun = Layer()

draw_animal()
show_animation()