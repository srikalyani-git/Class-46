class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def display(self):
        print("My Full Name Is:", self.fname+self.lname)

class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

student1 = student("John","Doe","2014")
student1.display()
print(student1.year, "is the year i graduated")