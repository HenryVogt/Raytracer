__author__ = 'Henry Vogt'


class Triangle(object):

    def __init__(self, a, b, c, material):
        self.a = a                  # Eckpunkt a
        self.b = b                  # Eckpunkt b
        self.c = c                  # Eckpunkt c
        self.u = self.b - self.a    # Vector
        self.v = self.c - self.a    # Vector
        self.material = material    # Material des Dreieck

    def __repr__(self):
        return 'Triangle(%s,%s,%s,%s)' % (repr(self.a),repr(self.b),repr(self.c),repr(self.material))

    def intersectionParameter(self, ray):   # Berechnung der Schnittstelle des Objekts mit dem Sichtstrahl
        w = ray.origin -self.a
        dv = ray.direction.cross(self.v)
        dvu = dv * self.u
        if dvu == 0.0:
            return None
        wu = w.cross(self.u)
        r = (dv * w) / dvu
        s = (wu * ray.direction) / dvu
        if 0<=r and r<=1 and 0<=s and s<=1 and r+s<=1:
            return (wu * self.v) / dvu
        else:
            return None

    def normalAt(self, p):
        return self.u.cross(self.v).normalized()

    def getMaterial(self):
        return self.material