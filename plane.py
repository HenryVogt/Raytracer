__author__ = 'Henry Vogt'


class Plane(object):

    def __init__(self, point, normal, material):
        self.point = point                  # Point der Ebene
        self.normal = normal.normalized()   # Vector der Ebene
        self.material = material            # Material der Ebene

    def __repr__(self):
        return 'Plane(%s,%s,%s)' % (repr(self.point),repr(self.normal),repr(self.material))

    def intersectionParameter(self, ray):   # Berechnung der Schnittstelle des Objekts mit dem Sichtstrahl
        op = ray.origin - self.point
        a = op * self.normal
        b = ray.direction * self.normal
        if b:
            return -a/b
        else:
            return None

    def normalAt(self, p):
        return self.normal

    def getMaterial(self):
        return self.material