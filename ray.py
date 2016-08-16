__author__ = 'Henry Vogt'


class Ray(object):

    def __init__(self, origin, direction):
        self.origin = origin                        # Ursprung des Strahls
        self.direction = direction.normalized()     # Vektor des Strahls

    def __repr__(self):
        return 'Ray(%s,%s)' %(repr(self.origin), repr(self.direction))

    def pointAtParameter(self, t):
        return self.origin + self.direction.scale(t)    # bestimme Punkt auf dem Strahl