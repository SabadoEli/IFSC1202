import math

class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        
        def type(self):
            if self.s1 == self.s2 == self.s3:
                return "Equilateral"
            elif self.s1 == self.s2 or self.s1 == self.s3 or self.s2 == self.s3:
                return "Isosceles"
            else:
                return "Scalene"
    def perimeter(self):
        return self.s1 + self.s2 + self.s3
    
    def area(self):
        s = (self.s1 + self.s2 + self.s3) / 2
        area = math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))
        return area
    
    
    