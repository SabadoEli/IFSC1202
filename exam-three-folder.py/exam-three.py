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
    
    def angles(self):
        angle1 = math.degrees(math.acos(min(max((self.s2**2 + self.s3**2 - self.s1**2) / (2 * self.s2 * self.s3), -1), 1)))
        angle2 = math.degrees(math.acos(min(max((self.s1**2 + self.s3**2 - self.s2**2) / (2 * self.s1 * self.s3), -1), 1)))
        angle3 = 180 - angle1 - angle2
        return [angle1, angle2, angle3]
    
def read_triangles_from_file(filename):
    triangles = []
    with open(filename, 'r') as file:
        for line in file:
            sides = list(map(float, line.strip().split(',')))
            triangle = Triangle(*sides)
            triangles.append(triangle)
    return triangles

def print_triangle_info(triangles):
    print(f"{'Type':<12}{'Side 1':<10}{'Side 2':<10}{'Side 3':<10}{'Perimeter':<12}{'Area':<10}{'Angle 1':<10}{'Angle 2':<10}{'Angle 3':<10}")
    for triangle in triangles:
        t_type = triangle.type()
        s1, s2, s3 = triangle.s1, triangle.s2, triangle.s3
        perimeter = triangle.perimeter()
        area = triangle.area()
        angles = triangle.angles()

        print(f"{t_type:<12}{s1:<10.3f}{s2:<10.3f}{s3:<10.3f}{perimeter:<12.3f}{area:<10.3f}{angles[0]:<10.3f}{angles[1]:<10.3f}{angles[2]:<10.3f}")
        
if __name__ == "__main__":
    triangles = read_triangles_from_file('exam-three-folder.py/Exam Three Triangles.txt')
    print_triangle_info(triangles)