__author__ = 'Henry Vogt'


class Material(object):

    def __init__(self, color, ka=0.7, kd=0.5, ks=0.3, shine=20.):
        self.color = color          # Materialfarbe oder Muster
        self.ka = ka                # ambienter Koeffizient
        self.kd = kd                # diffuser Koeffizient
        self.ks = ks                # spekularer Koeffizient
        self.shine = shine          # Lichtschein Exponent


    def calcAmb(self, color):
        ambColor = color * self.ka  # Multiplikation der Objektfarbe mit dem ambienten Koeffizient
        return ambColor

    def calcDif(self, cin, l, n):
        skalar = l * n
        colorDif = cin.getColor() * self.kd     # Multiplikation der Lichtfarbe mit dem diffusen Koeffizient
        return colorDif * skalar                # Multiplikation der diffusen Lichtfarbe mit dem Skalar von l und n

    def calcSpe(self, cin, l, n, rayDirection):
        lr = self.calcLr(l,n)
        skalar = lr * rayDirection.scale(-1.)
        colorSpe = cin.getColor() * self.ks     # Multiplikation der Lichtfarbe mit dem spekularen Koeffizient
        return colorSpe * (skalar**self.shine)  # Multiplikation der spekularen Lichtfarbe mit dem skalar von lr und - d

    def calcLr(self, l, n):
        skalar = n * l
        n = n.scale(2*skalar)
        return l - n

    def calcColor(self, color, cin, l, n, rayDirection):
        amb = self.calcAmb(color)
        dif = self.calcDif(cin, l, n)
        spe = self.calcSpe(cin, l, n, rayDirection.normalized())
        return amb+dif+spe

    def getColor(self):
        return self.color

    def getColorAt(self, p):
        return self.color.getColorAt(p)