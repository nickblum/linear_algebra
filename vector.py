import math

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
        # __str__ is what happens when calling print on the object
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        # __eq__ is what happens on when using comparison operators on the object
        return self.coordinates == v.coordinates

    def add(self, v):
        return Vector([sum(x) for x in zip(self.coordinates, v.coordinates)])
    
    def subtract(self, v):
        return Vector([x-y for x,y in zip(self.coordinates, v.coordinates)])

    def scalar_multiply(self, scalar):
        return Vector([x*scalar for x in self.coordinates])

    def magnitude(self):
        return math.sqrt(sum([x^2 for x in self.coordinates]))


"""
test_vec1 = Vector([1,2,3])
test_vec2 = Vector([-1,2,4])
print(test_vec1)
print(test_vec1.add(test_vec2))

print(Vector([8.218,-9.341]).add(Vector([-1.129,2.111])))
print(Vector([7.119,8.215]).subtract(Vector([-8.223,0.878])))
print(Vector([1.671,-1.012,-0.318]).scalar_multiply(7.41))
"""
print(Vector([-.221,7.437]).magnitude())