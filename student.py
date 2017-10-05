class Student:
    '''
        Student class keeps track of attendance, assignments
        Should contain

        Student has student ID, assignments, grade, attendence
    '''
    def __init__(self, lastName, firstName, studentID):
        self.lastName = lastName
        self.firstName = firstName
        self.studentID = studentID
        self.attendance = {}
        self.assignmentGrades = {}

    def updateGrade(self, assignment, grade):
        self.assignmentGrades[assignment] = grade
    
    def removeAssignment(self, assignment):
        del self.assignmentGrades[assignment]
    
    def getGrade(self):
        gradeTotal = 0
        for assignment in self.assignmentGrades:
            gradeTotal += self.assignmentGrades[assignment]
        return gradeTotal

    def getID(self):
        return self.studentID