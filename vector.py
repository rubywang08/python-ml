import math
from decimal import *

class Vector(object):

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self,v):
        #new_coordinates = [x+y for x,y in zip(self.coordinates,v.coordinates)]
        #return Vector(new_coordinates)
        list = []
        for i in range(self.dimension):
             item = self.coordinates[i] + v.coordinates[i]
             list.append(item)
        return Vector(list)

    def minus(self,v):
        list = []
        for i in range(self.dimension):
            item = self.coordinates[i] - v.coordinates[i]
            list.append(item)
        return Vector(list)

    def multiply(self,num):
        list = []
        for x in self.coordinates:
             item = x * num
             list.append(item)
        return Vector(list)

    def length(self):
        # list_squared = [x**2 for x in self.coordinates]
        # return math.sqrt(sum(list_squared))
        temp = 0
        for x in self.coordinates:
            temp = temp + x**2
        return temp.sqrt()

    def normalized(self):
        try:
            length = Decimal(self.length())
            return self.multiply(1/length)
        except ZeroDivisionError:
            raise Exception('Cannot nomalize the zero vector')

    def dot(self,v):
       new_coordinates = [x*y for x,y in zip(self.coordinates,v.coordinates)]
       return sum(new_coordinates)

    def angle(self,v,in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            cosO =u1.dot(u2)
            if in_degrees:
                degrees_per_radian = 180/math.pi
                return math.acos(cosO) * degrees_per_radian
            else:
                return math.acos(cosO)

        except Exception as e:
            if str(e) == 'Cannot nomalize the zero vector':
                raise Exception('Cannot calculte the angle with zero vector')
            else:
                raise e

    def isParalleOrOrthogonality(self,v,tolerance=1e-10):
        if (self.length() < tolerance) or (v.length() < tolerance):
            return "orthogonality and paralle"
        elif abs(self.dot(v)) < tolerance:
             return "orthogonality"
        elif (self.angle(v) == 0 or self.angle(v) == math.pi):
            return "paralle"
    #mentor code
    def is_orthogonal_to(self,v,tolerance=1e-10):
        return abs(self.dot(v)) < tolerance


    def is_zero(self,tolerance=1e-10):
        return self.length() < tolerance

    def is_parallel_to(self,v):
        return (self.is_zero() or v.is_zero() or self.angle(v) == 0 or self.angle(v)==math.pi)

    def paralle_to(self,v):
        u = v.normalized()
        return u.multiply(self.dot(u))

    def orthogonal_to(self,v):
        proj = self.paralle_to(v)
        return self.minus(proj)

    def cross_product(self,v):
        a = self.coordinates
        b = v.coordinates
        return Vector([a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]])
