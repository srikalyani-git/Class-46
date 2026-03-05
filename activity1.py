class person:
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    
    def display(self):
        print("My name is", self.name, "and my idnumber is", self.idnumber)

class extra(person):
    def __init__(self, name, idnumber, salary, role):
        person.__init__(self, name, idnumber)
        self.salary = salary
        self.role = role

per1 = extra("John","12345","$2500","Junior developer")
per1.display()