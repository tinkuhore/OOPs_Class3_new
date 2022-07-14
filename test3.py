class ineuron:
    def student(self):
        print('details of all the students')

    def achivers(self):
        print('list of all the achivers')

    def hall_of_fame(self):
        print('list of all from hall of fame')

class ineuron_vision(ineuron):
    def student(self):
        print('this are the filtered student list')

iv = ineuron_vision()
iv.student()