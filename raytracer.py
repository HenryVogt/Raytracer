__author__ = 'Henry Vogt'

import math
from ray import Ray
from checkerboard import Checkerboard


class Raytracer(object):

    def __init__(self, image, imageWidth, imageHeight, camera, backgroundColor, light, cin, objectlist):
        self.image = image                                      # Bildinstanz
        self.imageWidth = imageWidth                            # Bildbreite
        self.imageHeight = imageHeight                          # Bildhoehe
        self.camera = camera                                    # Kamerainstanz
        self.backgroundColor = backgroundColor                  # Hintergrundfarbe
        self.light = light                                      # Lightquelle
        self.cin = cin                                          # Lichtfarbe
        self.objectlist = objectlist                            # Liste der Objektinstanzen
        self.pixelWidth = 0                                     # Pixelbreite
        self.pixelHeight = 0                                    # Pixelhoehe
        self.width = 0                                          # Breite Projektionsflaeche
        self.height = 0                                         # Hoehe Projektionsflaeche

    def setup(self):
        aspectratio = self.imageWidth / self.imageHeight        # Seitenverhaeltnis
        self.height = 2*math.tan(self.camera.getFov()/2.)       # Hoehe Projektionsflaeche
        self.width = aspectratio*self.height                    # Breite Projektionsflaeche
        self.pixelWidth = self.width / (self.imageWidth-1)      # Pixelbreite
        self.pixelHeight = self.height / (self.imageHeight-1)   # Pixelhoehe

    def createImage(self):
        for x in range(int(self.imageWidth)):
            for y in range(int(self.imageHeight)):
                ray = self.camera.calcRay(x, y, self.pixelWidth, self.pixelHeight, self.width, self.height)     # erzeugen des Sichtstrahls
                maxdist = float('inf')
                color = self.backgroundColor    # setze Farbe auf Hintergrundfarbe
                for object in self.objectlist:
                    hitdist = object.intersectionParameter(ray)     # Distanz zum Schnittpunkt mit einem Objekt
                    if hitdist:
                        if hitdist < maxdist and hitdist > 0:

                            maxdist = hitdist
                            intersection = ray.pointAtParameter(hitdist-0.0001)     # Schnittpunkt des Strahls mit dem Object (-0.0001 Ausgleich Rundungsfehler)
                            lightRay = Ray(intersection, self.light - intersection) # Strahl vom Schnittpunkt zur Lichtquelle
                            normal = object.normalAt(intersection)                  # Normalenvektor am Schnittpunkt
                            material = object.getMaterial()     # Material der Objektinstanz

                            if self.hasShadow(lightRay):    # Untersuche Schnittpunkt auf Schatten
                                if isinstance(material.getColor(), Checkerboard):   # Wenn das Material ein Schachbrettmuster ist
                                    color = material.calcAmb(material.getColorAt(intersection))
                                else:
                                    color = material.calcAmb(material.getColor())
                            else:
                                if isinstance(material.getColor(), Checkerboard):   # Wenn das Material ein Schachbrettmuster ist
                                    color = material.calcColor(material.getColorAt(intersection), self.cin, lightRay.direction, normal, ray.direction)
                                else:
                                    color = material.calcColor(material.getColor(), self.cin, lightRay.direction, normal, ray.direction)

                self.image.putpixel((x,y), color.getValues())   # ersetze Pixel durch errechneten Farbwert

    def hasShadow(self, lightRay):
        for object in self.objectlist:
            hitdist = object.intersectionParameter(lightRay)
            if hitdist and hitdist > 0:     # wenn der Strahl vom Schnittpunkt zur Lichtquelle ein Objekt trifft wird Schatten erzeugt
                return True
        return False