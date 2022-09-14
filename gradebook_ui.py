from gradebook import Gradebook
from student import Student
import pathlib

class GradebookUI:
    def __init__(self) -> None:
        self.__gradebook = Gradebook()
    
    def newSemester(self):
        self.__gradebook.newSemester()
    
    def addStudent(self, studentID: int, firstName: str, lastName: str):
        self.__gradebook.addStudent(studentID, firstName, lastName)
    
    def recordScores(self, type: str):
        self.__gradebook.recordScores(type)

    def changeScores(self):
        self.__gradebook.changeScores()
    
    def finalScores(self):
        self.__gradebook.finalScores()
    
    def outputData(self, method: str):
        self.__gradebook.outputData(method)
    
    def saveStudents(self):
        self.__gradebook.saveStudents()

    def showTitle(self):
        print("******The Grade Book*******")

    def showMenu(self):
        print("\nCommand Menu")
        print("S - Set Up New Semester")
        print("A - Add a Student")
        print("P - Record Programming Assignment Score")
        print("T - Record Test Score")
        print("F - Record Final Exam")
        print("C - Change Grade")
        print("G - Calculate Final Score")
        print("O - Output Grade Data")
        print("Q - Exit Program")

def main():
    file = pathlib.Path("Grades_dat.csv")
    if file.exists() == False:
        with open('Grades_dat.csv', 'w', newline = "") as file:
            pass
    gb = GradebookUI()
    gb.showTitle()
    file = pathlib.Path("policies.csv")

    while True:
        gb.showMenu()
        command = input("Please enter a command: ")
        if command == 'S':
            print()
            print("------Set Up New Semester-----")
            semester = input("Semester/Year:")
            gb.newSemester()
        elif command == 'A':
            if file.exists() == False:
                raise KeyError("Please Set Up New Semester.")
            print()
            print("------Add a Student-----")
            studentInfo = input("Please enter Student ID, First and Last Name (Separated by comma): ")
            studentInfoArray = studentInfo.split(",")
            gb.addStudent(int(studentInfoArray[0]), studentInfoArray[1], studentInfoArray[2])
        elif command == 'P':
            if file.exists() == False:
                raise KeyError("Please Set Up New Semester.")
            print()
            print("------Record Programming Assignment Score-----")

            gb.recordScores('P')
        elif command == 'T':
            if file.exists() == False:
                raise KeyError("Please Set Up New Semester.")            
            print()
            print("------Record Test Score-----")
            gb.recordScores('T')
        elif command == 'F':
            if file.exists() == False:
                raise KeyError("Please Set Up New Semester.")
            print()
            print("------Record Final Exam Score-----")
            gb.recordScores('F')    
        elif command == 'C':
            if file.exists() == False:
                raise KeyError("Please Set Up New Semester.")
            print()
            print("------Change a Grade-----")
            gb.changeScores()  
        elif command == 'G':
            if file.exists() == False:
                raise KeyError("Please Set Up New Semester.")
            print()
            print("------Calculate Final Grade-----")
            gb.finalScores()
        elif command == 'O':
            if file.exists() == False:
                raise KeyError("Please Set Up New Semester.")
            print()
            print("------Output Grade Data-----")
            method = input("Order by 'Name' or 'ID'? ")
            gb.outputData(method)
        elif command == 'Q':
            if file.exists() == False:
                raise KeyError("Please Set Up New Semester.")
            print()
            print("------Quit-----")
            gb.saveStudents()
            break
        else:
            raise ValueError("Invalid Command")                                               

if __name__ == "__main__":
    main()