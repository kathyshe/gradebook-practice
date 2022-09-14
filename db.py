from asyncio.windows_events import NULL
from student import Student
import csv
import pathlib

class StudentRepository:
    def __init__(self):
        self.__filename = "Grades_dat.csv"

    def getStudents(self) -> list[Student]:
        students: list[Student] = []
        with open(self.__filename, newline = "") as file:
            reader = csv.reader(file)
            for row in reader:
                student = Student (
                    int(row[0]),
                    row[1],
                    row[2],
                    list(row[3:(len(row) - 1)]),
                    row[len(row) - 1]
                )
                students.append(student)
        
        return students
    
    def saveStudents(self, students: list[Student]):
        with open(self.__filename, 'w', newline = "") as file:
            writer = csv.writer(file)
            for student in students:
                writer.writerow(student.getStudentInfo())
        #write to customers.csv file


# def main():
#     repo = StudentRepository()
#     students = repo.getStudents()
#     for student in students:
#         print(student)
    
#     scores = [0] * 3
#     student = Student(233, "Kelly", "Li", scores)
#     student.addscore(2.3, 0)
#     student.addscore(5.0, 1)
#     student.addscore(5.0, 2)
#     students.append(student)

#     repo.saveStudents(students)
#     for student in students:
#         print(student)

# if __name__ == "__main__":
#     main()