class Student:
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def getName(self):
        return self.name
        
    def getGrade(self):
        return self.grade

def main():
    
    file = open("studentFile.txt", "r")
    line = file.readline()
    name, age, grade = line.split(" ")
    best = Student(name, int(age), int(grade))
    
    for line in file:
        name, age, grade = line.split(" ")
        student = Student(name, int(age), int(grade))
       
        #if this student is best so far, remember it.
        if student.getGrade() > best.getGrade():
            best = student
            
    print("Best GPA is",best.getName(),"with a GPA of", best.getGrade())
    
    file.close()
    
main()
