import math

class Point2D:
    def __init__(self, x, y):
        self.a = x
        self.b = y
    
    def compute_distance(self, other):
        return math.sqrt((self.a - other.a)**2 + (self.b - other.b)**2)
    
    def distance_between(self, p):
        if isinstance(p, Point2D):
            return math.sqrt((self.a - p.a)**2 + (self.b - p.b)**2)
        return NotImplemented
    
    def __str__(self):
        return f"Point is ({self.a, self.b})"

    def __sub__(self, p):
        return Point2D(self.a - p.a, self.b - p.b)
    
    def __mul__(self, p):
        if isinstance(p, Point2D):
            return Point2D(self.a * p.a, self.b * p.b)
        else:
            return Point2D(p*self.a, p*self.b)


p1 = Point2D(12, 32)
p2 = Point2D(2, 3)

print(f'Distance b/w the two points ({p1.a}, {p1.b}) and ({p2.a}, {p2.b}) = '
      f'{p1.compute_distance(p2)}')

print(f'Distance b/w the two points ({p1.a}, {p1.b}) and (5, 7) = '
      f'{p1.distance_between((5,7))}')

print(f'Distance b/w the two points ({p1.a}, {p1.b}) and (5, 7) = '
      f'{p1.distance_between(Point2D(5,7))}')


print(f'p1 x p2 = {p1*p2}')
print(f'p1 - p2 = {p1-p2}')
print(f'p1 x 5 = {p1*5}')

