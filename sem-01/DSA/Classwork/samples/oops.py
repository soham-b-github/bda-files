from math import sqrt as sq


def dist_from_origin(p):
    return sq(p[0]**2 + p[1]**2)

def dist_between(x,y):
    return sq((y[1] - x[1])**2 + (y[0] - x[0])**2 )



class Point2D:
    insts = 0
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        Point2D.insts +=1

    def distance_from_origin(self):
        return sq(self.x**2 + self.y**2)

    def distance_between(self,p):
        return sq((self.x - p.x)**2 + (self.y - p.y)**2) 
  
    def __add__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.x + other.x, self.y+other.y)
        return NotImplemented

    def __str__(self):
        return f" x, y are: {self.x}, {self.y}"
    
    def __sub__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.x-other.x, self.y-other.y)
        return NotImplemented
    
    # def __mul__(self, s):
        # for scalar multiplication
        # return Point2D(s*self.x, s*self.y)
    
    def __mul__(self, other):
        if(isinstance(other, Point2D)):
            return (self.x*other.x, self.y*other.y)
        else:
            return (other*self.x, other*self.y)



class Point3D(Point2D):
    def __init__(self,x,y,z):
        super().__init__(x, y)
        self.z = z

    def distance_from_origin(self):
       return sq(self.x**2 + self.y**2 + self.z**2)

    def __str__(self):
        return f" x, y, z are: {self.x}, {self.y}, {self.z}"


if __name__ == '__main__':
    p1 = (4,5)
    p2 = (1,1)
    # print(dist_from_origin(p2))
    # print(dist_between(p1,p2))
    p1 = Point2D(4,5)
    p2 = Point2D(3,-2)
    res = p1 + p2
    
    # print('result after addition is', res)
    # print(p2.distance_from_origin())
    # print(p1.distance_between(p2))

    #scalar multiplication
    a = 3
    print(f'Multiplying ({p1.x},{p1.y}) with {a} = {p1*3}')

    #component-wise vector multiplication
    print(f'Multiplying ({p1.x},{p1.y}) with ({p2.x},{p2.y}) = ',p1*p2)
    
    p3 = Point3D(4, 7, 8)
    
    # print(p3.distance_from_origin())
    # print(p3)
    # print('total instances are ', Point2D.insts)