from student import Student
from db import StudentRepository
import csv

class Gradebook:
    def __init__(self) -> None:
        self.__db = StudentRepository()
        self.__students: list[Student] = self.__db.getStudents()

    @property
    def students(self) -> list[Student]:
        return self.__students

    def addStudent(self, studentID: int, firstName: str, lastName:str):
        for student in self.__students:
            if student.studentID == studentID:
                raise KeyError("Duplicate Student ID")
        policies = self.readPolicies() 
        numAssignments = policies[0] + policies[2] + policies[4]
        student = Student(studentID, firstName, lastName, [0] * numAssignments)
        print(student)
        self.__students.append(student)
        self.saveStudents()
    
    def saveStudents(self):
        self.__db.saveStudents(self.__students)
    
    def recordScores(self, type: str):
        policies = self.readPolicies()

        def findStudent(assignmentNumber: int):
            for student in self.__students:
                print("Student ID: " + str(student.studentID) + ", Student Name: " + student.firstName + " " + student.lastName)
                score = float(input("Input Score: "))
                student.addscore(score, assignmentNumber)
                self.saveStudents()

        if type == 'P':
            number = int(input("Assignment number:"))
            if number > policies[0]:
                raise ValueError("Invalid Assignment Number")
            findStudent(number - 1)

        elif type == 'T':
            number = int(input("Test number: "))
            if number > policies[2]:
                raise ValueError("Invalid Test Number")
            findStudent(number + policies[0] - 1)

        elif type == 'F':
            findStudent(policies[0] + policies[2] + policies[4] - 1)

    def changeScores(self):
        policies = self.readPolicies()
        studentID = int(input("Student ID: "))
        newScore = float(input("New Score: "))
        type = input("Type of Scores (P/T/F): ")
        for student in self.__students:
            if student.studentID == studentID:
                if type == 'P':
                    number = int(input("Assignment number to change: "))
                    student.addscore(newScore, number - 1)
                elif type == 'T':
                    number = int(input("Test number to change: "))
                    student.addscore(newScore, policies[0] + number - 1)
                elif type == 'F':
                    student.addscore(newScore, policies[0] + policies[2] + policies[4] - 1)
                else:
                    raise ValueError("Invalid input.")
                self.saveStudents()
                return
        raise KeyError("Student not found!")

    def finalScores(self):
        policies = self.readPolicies()
        numOfAssignment = policies[0]
        numOfTest = policies[2]
        numOfExam = policies[4]
        for student in self.__students:
            assignmentScore = 0
            testScore = 0
            examScore = 0
            for x in range(numOfAssignment):
                assignmentScore = assignmentScore + float(student.scores[x])
            assignmentScore = assignmentScore * (policies[1] / 100) / numOfAssignment
            for x in range(numOfTest):
                testScore += float(student.scores[x + numOfAssignment])
            testScore = testScore * (policies[3] / 100) / numOfTest
            for x in range(numOfExam):
                examScore = float(student.scores[x + numOfAssignment + numOfTest]) * (policies[5] / 100)
            finalScore = assignmentScore + testScore + examScore
            student.finalScore = finalScore
            self.saveStudents()

    def readPolicies(self) -> list[int]:
        policies = []
        with open('policies.csv', 'r', newline = "") as file:
            policiesInfo = file.readlines()[1]
        policiesArray = policiesInfo.split(",")
        for policy in policiesArray:
            policies.append(int(policy))
        return policies

    def savePolicies(self, info: list[str]):
        header = ['Programming Assignment', 'Weight', 'Tests', 'Weight', 'Final Exam', 'Weight']
        with open('policies.csv', 'w', newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerow(info)

    def newSemester(self):
        info: list[str] = []
        programAssign = int(input("Please enter number of programming assignments (0-6): "))
        pWeight = int(input("Total % weights for programming assignments: "))
        print("Each programming assignment weight is (%): ", float(pWeight / programAssign))
        tests = int(input("Please enter number of tests (0-4): "))
        tWeight = int(input("Total % weights for tests: "))
        print("Each test weight is (%): ", float(tWeight / tests))
        finalExams = int(input("Please enter number of final exams (0-1): "))
        info.append(programAssign)
        info.append(pWeight)
        info.append(tests)
        info.append(tWeight)
        info.append(finalExams)
        if finalExams == 0:
            if pWeight + tWeight != 100:
                raise ValueError("Relative Weights must add up to 100%")
        if finalExams == 1:
            fWeight = int(input("Total % weights for final exam: "))
            if pWeight + tWeight + fWeight != 100:
                raise ValueError("Relative Weights must add up to 100%")                
            info.append(fWeight)
        self.savePolicies(info)

    def outputData(self, method:str):
        policies = self.readPolicies()

        def lastName(student:Student) -> str:
            return student.lastName

        def id(student:Student) -> int:
            return student.studentID

        if method == 'Name':
            studentsInfo = sorted(self.__students, key=lastName)
        elif method == 'ID':
            studentsInfo = sorted(self.__students, key=id)
        # print(studentsInfo[0])
        header0 = ['PA = Programming Assignment']
        header1 = ['Student ID', 'First Name', 'Last Name']
        for x in range(policies[0]):
            header1.append('PA' + str(x + 1))
        for x in range(policies[2]):
            header1.append('Test' + str(x + 1))
        for x in range(policies[4]):
            header1.append('Final Exam')
        header1.append('Final Score')

        with open('Grades_out.csv', 'w', newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(header0)
            writer.writerow(header1)
            for student in studentsInfo:
                writer.writerow(student.getStudentInfo())


def main():
    gb_b = Gradebook()
    # policies = gb_b.readPolicies('FA22')
    # print(policies)
    policies = gb_b.readPolicies()
    print(policies)
    gb_b.outputData('Name')

if __name__ == "__main__":
    main()