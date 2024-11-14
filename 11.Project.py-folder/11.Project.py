class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []
    def RunningAverage(self):
            valid_grades = [int(grade) for grade in self.Grades if grade != ""]
            if not valid_grades:
                return 0
            return sum(valid_grades) / len(valid_grades)
   
    def TotalAverage(self):
        total_grades = [float(grade) if grade != "" else 0 for grade in self.Grades]
        if not total_grades:
            return 0
        return sum(total_grades) / len(total_grades)
    
    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
        
class StudentList:
    def __init__(self):
        self.Studentlist = []
        
    def add_student(self, firstname, lastname, tnumber):
        student = Student(firstname, lastname, tnumber)
        self.Studentlist.append(student)
    def find_student(self, tnumber):
        for index, student in enumerate(self.Studentlist):
            if student.TNumber == tnumber:
                return index
        return -1
    
    def print_student_list(self):
        print(f"{'First Name':<12}{'Last Name':<12}{'ID':<12}{'Running Avg':<12}{'Semester Avg':<12}{'Letter Grade':<12}")
        print(f"{'-'*12}{'-'*12}{'-'*12}{'-'*12}{'-'*12}{'-'*12}")
        for student in self.Studentlist:
            print(f"{student.FirstName:<12}{student.LastName:<12}{student.TNumber:<12}"
              f"{student.RunningAverage():<12.2f}{student.TotalAverage():<12.2f}"
              f"{student.LetterGrade():<12}")
            
    def add_student_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                firstname, lastname, tnumber = line.strip().split(',')
                self.add_student(firstname, lastname, tnumber)
    
    def add_scores_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                tnumber, score = line.strip().split(',')
                index = self.find_student(tnumber)
                if index != -1:
                    if score:
                        self.Studentlist[index].Grades.append(score)
                    else:
                        self.Studentlist[index].Grades.append("0")
                    
student_list = StudentList()
student_list.add_student_from_file("11.Project.py-folder/11.Project Students.txt")
student_list.add_scores_from_file("11.Project.py-folder/11.Project Scores.txt")
student_list.print_student_list()