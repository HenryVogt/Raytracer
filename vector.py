__author__ = 'Henry Vogt'

import math
import point


class Vector(object):

    def __init__(self,*coords):
        self.coords = ()    # Koordinaten des Vektors in float Werten
        for e in coords:
            self.coords += (float(e),)

    def getCoords(self):
        return self.coords

    def __repr__(self):
        return 'Vector%s' % (repr(self.coords))

    def normalized(self):       # gibt einen neuen Vector mit den normalisierten Koordinaten der Vectorinstanz zurueck
        x = 1/self.getLength()
        normalized_coords = ()
        for e in self.coords:
            normalized_coords += (x*e,)
        return Vector(*normalized_coords)

    def getLength(self):
        return math.sqrt(sum(i*i for i in self.coords))

    def scale(self,t):          # gibt einen neuen Vector mit den skalierten Koordinaten der Vectorinstanz zurueck
        scaled_coords = ()
        for e in self.coords:
            scaled_coords += (t*e,)
        return Vector(*scaled_coords)

    def __add__(self, other):   # Addition mit Vector oder Point
        if isinstance(other, Vector): # wenn mit Vector addiert wird = neuer Vector
            new_coords = tuple([x+y for (x,y) in zip(self.coords,other.getCoords())])
            return Vector(*new_coords)
        elif isinstance(other, point.Point): # wenn mit Point addiert wird = neuer Point
            new_coords = tuple([x+y for (x,y) in zip(self.coords,other.getCoords())])
            return point.Point(*new_coords)

    def __mul__(self, other):   # Multiplikation mit Vector
        if isinstance(other,Vector):
            return sum([x*y for (x,y) in zip(self.coords,other.getCoords())])

    def __sub__(self, other):   # Subtraktion mit Vector
        if isinstance(other,Vector):
            new_coords = tuple([x-y for (x,y) in zip(self.coords,other.getCoords())])
            return Vector(*new_coords)

    def cross(self,other):      # Kreuzprodukt mit Vector
        x = self.coords[1]*other.getCoords()[2]-self.coords[2]*other.getCoords()[1]
        y = self.coords[2]*other.getCoords()[0]-self.coords[0]*other.getCoords()[2]
        z = self.coords[0]*other.getCoords()[1]-self.coords[1]*other.getCoords()[0]
        return Vector(x,y,z)
