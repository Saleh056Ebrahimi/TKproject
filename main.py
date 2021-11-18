import fileinput
import os


# noinspection PyAttributeOutsideInit
class student:

    def file_name(self, item):
        self.fname = item

    def first_name(self, item):
        self.firstName = item
        f = open(self.fname, 'x')
        f.write('FirstName:' + self.firstName + '\n')

    def last_name(self, item):
        self.lastName = item
        f = open(self.fname, 'a')
        f.write('LastName:' + self.lastName + '\n')

    def father_name(self, item):
        self.fatherName = item
        f = open(self.fname, 'a')
        f.write('FatherName:' + self.fatherName + '\n')

    def student_code(self, item):
        self.studentCode = item
        f = open(self.fname, 'a')
        f.write('StudentCode:' + self.studentCode)


class manipulating_studnet:

    def students_file(self, item):
        f = open('students_codes.txt', 'a')
        f.write(item + '\n')

    def addStudent(self, item):
        for i in range(item):
            print('please enter the new file name for keeping new information...')
            x = str(input('use the student ID of new student:') + '_student.txt')

            self.students_file(x)

            s = student()
            s.file_name(x)
            print('please enter the information of new student:')

            s.first_name(input('Name:'))
            s.last_name(input('LastName:'))
            s.father_name(input('FatherName:'))
            s.student_code(input('StudentCode:'))

    def removeStudnet(self, item):

        if os.path.exists(item):
            os.remove(item)
        else:
            print("The student does not exist")

    def change(self, item):

        print("enter Text to search for:")
        textToSearch = input("> ")

        print("Text to replace it with:")
        textToReplace = input("> ")

        # print ("File to perform Search-Replace on:")
        fileToSearch = item

        tempFile = open(fileToSearch, 'r+')

        for line in fileinput.input(fileToSearch):
            tempFile.write(line.replace(textToSearch, textToReplace))

        tempFile.close()


master = manipulating_studnet()
# master.addStudent(2)
# master.removeStudnet('97249801_student.txt')
# master.change('97149113_student.txt')
