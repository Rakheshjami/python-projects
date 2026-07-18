class person:
    university="codegnan university"
    def __init__(self,name,age,dept):
        self.name=name
        self.age=age
        self.dept=dept
    def display_info(self):
        pass

class student(person):
    student_count=0
    def __init__(self,name,age,dept,stuid,fees):
        super().__init__(name,age,dept)
        self.stuid=stuid
        self.fees=fees
        student.student_count+=1
    def display_info(self):
        print(f"Student_name:{self.name}\nage:{self.age}\nDepartment:{self.dept}\nstudent_id:{self.stuid}\nfees:{self.fees}")
class faculty(person):
    faculty_count=0
    def __init__(self,name,age,dept,facid,exp):
        super().__init__(name,age,dept)
        self.facid=facid
        self.exp=exp
        faculty.faculty_count+=1
    def display_info(self):
        print(f"faculty name:{self.name}\nage:{self.age}\nDepartment:{self.dept}\nfaculty_id:{self.facid}\nexperiance:{self.exp}")
class labassistant(person):
    def __init__(self,name,age,dept,employeeid,labname):
        super().__init__(name,age,dept)
        self.employeeid=employeeid
        self.labname=labname
    def display_info(self):
        print(f"Labassistant name:{self.name}\nage:{self.age}\nDepartment:{self.dept}\nemployeeid:{self.employeeid}\nLabname:{self.labname}")
class librarian(person):
    def __init__(self,name,age,dept,employeeid):
        super().__init__(name,age,dept)
        self.employeeid=employeeid
    def display_info(self):
        print(f"Librarian name:{self.name}\nage:{self.age}\nDepartment:{self.dept}\nemployeeid:{self.employeeid}")
class watchman(person):
    def __init__(self,name,age,dept,employeeid,shift):
        super().__init__(name,age,dept)
        self.employeeid=employeeid
        self.shift=shift
    def display_info(self):
        print(f"Watchman name:{self.name}\nage:{self.age}\nDepartment:{self.dept}\nemployeeid:{self.employeeid}\nShift:{self.shift}")
stu=student("rakesh",21,"CSE",573,50000)
stu.display_info()
fac=faculty("Nikhil",45,"CSE",567,5)
fac.display_info()
lab=labassistant("kaushik",30,"CSE",5678,"Clab")
lab.display_info()
lib=librarian("Sekhar",30,"CSE",5678)
lib.display_info()

















