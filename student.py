class Student:
    def __init__(self, studentID: int, firstName: str, lastName: str, scores: list[float], finalScore: float = -1): 
        self.__studentID = studentID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__scores = scores
        self.__finalScore = finalScore
    
    
    def addscore(self, score: float, index: int):
        self.__scores[index] = score

    @property
    def studentID(self) -> int:
        return self.__studentID

    @studentID.setter
    def studentID(self, studentID: int) -> None:
        self.__studentID = studentID
    
    @property
    def firstName(self) -> str:
        return self.__firstName
    
    @firstName.setter
    def firstName(self, firstName: str) -> None:
        self.__firstName = firstName
    
    @property
    def lastName(self) -> str:
        return self.__lastName
    
    @lastName.setter
    def lastName(self, lastName: str) -> None:
        self.__lastName = lastName

    @property
    def scores(self) -> list[float]:
        return self.__scores

    @scores.setter
    def scores(self, scores: list[float]) -> None:
        self.__scores = scores

    def getStudentInfo(self) -> list[str]:
        line = []
        line.append(self.__studentID)
        line.append(self.__firstName)
        line.append(self.__lastName)
        line = line + self.scores
        line.append(self.__finalScore)
        return line
    
    @property
    def finalScore(self) -> float:
        return self.__finalScore
    
    @finalScore.setter
    def finalScore(self, finalScore: float):
        self.__finalScore = finalScore

    def __str__(self) -> str:
        output = "Student ID: " + str(self.studentID) + ", First Name: " + self.firstName + ", Last Name: " + self.lastName + ", Scores: "
        for score in self.scores:
            output += str(score) + ", "
        return output

def main():
    kathy = Student(555,'Karina','She',[0,0,0,0,0,0])
    kathy.addscore(80,5)
    print(kathy.scores)

if __name__ == "__main__":
    main()