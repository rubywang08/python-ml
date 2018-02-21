from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 30


class Plane(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 3

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()


    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = [Decimal('0')]*self.dimension

            initial_index = Plane.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e


    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Plane.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output


    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)

    def is_parallel(self, plane):
        v1 = Vector(self.normal_vector)
        v2 = Vector(plane.normal_vector)
        return v1.is_parallel_to(v2)

    def is_equal(self, plane):
        if self.is_parallel(plane):
            n = self.basepoint.minus(plane.basepoint)
            v1 = Vector(self.normal_vector)
            return n.is_orthogonal_to(v1)
        else:
            return False

class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


lan1 = Plane([Decimal("-0.412"), Decimal("3.806"), Decimal("0.728")], Decimal("-3.46"))
lan2 = Plane([Decimal("1.03"), Decimal("-9.515"), Decimal("-1.82")], Decimal("8.65"))

lan3 = Plane([Decimal("2.611"), Decimal("5.528"), Decimal("0.283")], Decimal("4.6"))
lan4 = Plane([Decimal("7.715"), Decimal("8.306"), Decimal("5.342")], Decimal("3.76"))

lan5 = Plane([Decimal("-7.926"), Decimal("8.625"), Decimal("-7.212")], Decimal("-7.952"))
lan6 = Plane([Decimal("-2.642"), Decimal("2.875"), Decimal("-2.404")], Decimal("-2.443"))

print lan1.is_parallel(lan2)
print lan1.is_equal(lan2)

print lan3.is_parallel(lan4)
print lan3.is_equal(lan4)

print lan5.is_parallel(lan6)
print lan5.is_equal(lan6)
