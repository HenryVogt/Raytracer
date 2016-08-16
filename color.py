__author__ = 'Henry Vogt'


class Color(object):

    def __init__(self, *values):
        self.values = values        # RGB Farbwerte

    def __repr__(self):
        return 'Color%s' % (repr(self.values))

    # Multiplikation mit Faktor
    def __mul__(self, faktor):
        new_values = tuple([int(x*faktor) for x in self.values])    # Multiplikation der Farbwerte um einen Faktor
        return Color(*new_values)

    def getValues(self):
        return self.values

    def __add__(self, other):
        new_values = tuple([x+y for (x,y) in zip(self.values,other.getValues())])   # Addition der Farbwerte mit einem Wert
        return Color(*new_values)