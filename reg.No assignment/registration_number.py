class Student:
    def __init__(self, name, reg_no):
        self.name= name
        self.reg_no= reg_no

    def display_info (self):
        print (f"Student Name: {self.name}")
        print (f"student reg_no: {self.reg_no}")

studentOne= Student("Joseph", "B242674")
result = studentOne.display_info()
print(result)
