__author__ = 'Henry Vogt'

from PIL import Image # importiert Image von Pillow
from vector import Vector
from point import Point
from camera import Camera
from sphere import Sphere
from plane import Plane
from triangle import Triangle
from color import Color
from material import Material
from raytracer import Raytracer
from checkerboard import Checkerboard


# Bildparameter
_WIDTH = 400.
_HEIGHT = 400.
_BACKGROUND = Color(0,0,0) # RGB

# Kameraparameter
_EYE = Point(0,2,5)
_UP = Vector(0,1,0)
_CENTER = Point(0,1,8)
_FIELD_OF_VIEW = 45

# Lichtparameter
_LIGHT = Point(-20,-20,3)
_CIN = Material(Color(255,255,255))

if __name__ == '__main__':

    # Erzeugen der Bild Instanz
    image = Image.new('RGB',(int(_WIDTH),int(_HEIGHT)))

    # Kamerainstanz
    camera = Camera(_EYE,_UP,_CENTER,_FIELD_OF_VIEW)

    # Objektinstanzen
    sphere1 = Sphere(Point(2.5,1,17),1.9,Material(Color(0,255,0)))
    sphere2 = Sphere(Point(-2.5, 1, 17),1.9,Material(Color(255,0,0)))
    sphere3 = Sphere(Point(0, -3.0, 17),1.9,Material(Color(0,0,255)))
    triangle = Triangle(Point(2.5,1,17),Point(0, -3.0, 17),Point(-2.5, 1, 17),Material(Color(255,255,0)))
    plane = Plane(Point(0, 3.5, 0), Vector(0,-1,0),Material(Checkerboard()))

    # Liste der Objektinstanzen
    objectlist = []
    objectlist.append(sphere1)
    objectlist.append(sphere2)
    objectlist.append(sphere3)
    objectlist.append(triangle)
    objectlist.append(plane)

    # Raytracer
    tracer = Raytracer(image, _WIDTH, _HEIGHT, camera, _BACKGROUND, _LIGHT, _CIN, objectlist)
    tracer.setup()
    tracer.createImage()

    # Ausgabe Bild
    image.show()
    image.save("image.jpg")

