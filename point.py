__author__ = 'Henry Vogt'

import vector


class Point(object):

    def __init__(self,*coords):
        self.coords = ()     # Koordinaten des Punkts in float Werten
        for e in coords:
            self.coords += (float(e),)

    def getCoords(self):
        return self.coords

    def __repr__(self):
        return 'Point%s' % (repr(self.coords))

    def __add__(self, other):       # Addition mit Vector
        if isinstance(other, vector.Vector):
            new_coords = tuple([x+y for (x,y) in zip(self.coords,other.getCoords())])
            return Point(*new_coords)

    def __sub__(self, other):       # Subtraktion mit Point
        if isinstance(other,Point):
            new_coords = tuple([x-y for (x,y) in zip(self.coords,other.getCoords())])
            return vector.Vector(*new_coords)