class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.firstname = firstname
        self.lastname = lastname
        self.tnumber = tnumber
        self.grades = scores 
    def RunningAverage(self):
        valid_scores = [float(score)for score in self.grades if score]
        return sum(valid_scores) / len(valid_scores) if valid_scores else 0.0
    def TotalAverage(self):
        total_scores = [float(score)if score else 0.0 for score in self.grades]
        return sum(total_scores) / len(total_scores)
    
    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
        
def main():
    students = []
    with open("10.Project.py-folder/10.Project Student Scores.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            firstname = parts[0].strip()
            lastname = parts[1].strip()
            tnumber = parts[2].strip()
            scores = parts[3:] 
            student = Student(firstname, lastname, tnumber, scores)
            students.append(student)
    print(f"{'First Name':<15}{'Last Name':<15}{'ID':<12}{'Running Avg':<12}{'Semester Avg':<12}{'Letter Grade'}")
    print('-' * 75)
    
    for student in students:
        running_avg = student.RunningAverage()
        semester_avg = student.TotalAverage()
        letter_grade = student.LetterGrade()
        print(f"{student.firstname:<15}{student.lastname:<15}{student.tnumber:<12}{running_avg:<12.2f}{semester_avg:<12.2f}{letter_grade}")
        
if __name__ == "__main__":
    main()

            
            
            