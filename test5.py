class ineuron:
    def __init__(self):
        self.student = 'data science'

    def students(self):
        print(self.student)

i = ineuron()
i.students()
i.student = 'data analysts'
i.students()

class ineuron1:
    def __init__(self):
        self.__student = 'data science'

    def students(self):
        print(self.__student)
    def sstudent_change(self, new_value):
        self.__student = new_value

i1 = ineuron1()
i1.students()
i1.sstudent_change('big data')
i1.students()