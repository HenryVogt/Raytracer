__author__ = 'Henry Vogt'

from color import Color
from vector import Vector

class Checkerboard(object):

    def __init__(self):
        self.color = Color(255,255,255)
        self.otherColor = Color(0,0,0)
        self.checkSize = 1

    def getColorAt(self, p):
        coords = p.getCoords()          # Koordinaten des uebergebenen Punkts
        v = Vector(*coords)             # Vektor aus den Koordinaten des Punkts
        v.scale(1. / self.checkSize)    # Groesse des Quadrats
        if (int(abs(v.getCoords()[0]) +0.5) + int(abs(v.getCoords()[1]) + 0.5) + int(abs(v.getCoords()[2]) + 0.5)) %2:
            return self.otherColor
        return self.color