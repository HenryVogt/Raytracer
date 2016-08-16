__author__ = 'Henry Vogt'

from vector import Vector
from ray import Ray


class Camera(object):

    def __init__(self, eye, up, center, fov):
        self.eye = eye              # Ursprungspunkt der Kamera
        self.up = up                # Oben
        self.center = center        # Zentrum auf das die Kamera gerichtet ist
        self.fov = fov              # Sichtfeld der Kamera
        self.f = self.calcF()       # Vektor f
        self.s = self.calcS()       # Vektor s
        self.u = self.calcU()       # Vektor u

    def __repr__(self):
        return 'Camera(%s,%s,%s,%s)' % (repr(self.eye),repr(self.up),repr(self.center),repr(self.fov))

    def calcF(self):
        vec = self.center - self.eye                                        # Vektor vom Kameraursprung zum Zentrum
        new_coords = tuple([x/vec.getLength() for x in vec.getCoords()])    # Einheitsvektor f
        return Vector(*new_coords)

    def calcS(self):
        vec = self.f.cross(self.up)                                         # Kreuzprodukt von Vektor f und Vektor up
        new_coords = tuple([x/vec.getLength() for x in vec.getCoords()])    # Einheitsvektor s
        return Vector(*new_coords)

    def calcU(self):
        return self.s.cross(self.f)                                         # Kreuzprodukt von Vektor s und Vektor f

    def calcRay(self, x, y, pixelWidth, pixelHeight, width, height):
        xcomp = self.s.scale(x*pixelWidth - width/2)                        # Ausrichtung der Kamera auf der x-Achse
        ycomp = self.u.scale(y*pixelHeight - height/2)                      # Ausrichtung der Kamera auf der y-Achse
        return Ray(self.eye, self.f + xcomp + ycomp)                        # Sichtstrahl der Kamera

    def getFov(self):
        return self.fov




