__author__ = 'Henry Vogt'

import math


class Sphere(object):

    def __init__(self, center, radius, material):
        self.center = center            # Zentrum der Kugel
        self.radius = float(radius)     # Radius der Kugel
        self.material = material        # Material der Kugel

    def __repr__(self):
        return 'Sphere(%s,%s,%s)' % (repr(self.center),repr(self.radius),repr(self.material))

    def intersectionParameter(self, ray):   # Berechnung der Schnittstelle des Objekts mit dem Sichtstrahl
        co = self.center - ray.origin
        v = co * ray.direction
        discriminant = v*v - co * co + self.radius*self.radius
        if discriminant < 0:
            return None
        else:
            return v - math.sqrt(discriminant)

    def normalAt(self, p):
        return (p - self.center).normalized()

    def getMaterial(self):
        return self.material
