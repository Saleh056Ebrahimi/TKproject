# یک برنامه دستکتاپ با tkinter بنویسید که اطلاعات یک دانشجو را دریافت می کند و در فایل ذخیره سازی می کند.  باید
# بتواند اطلاعات تعدادی دانشجو را ذخیره و بر اساس شماره دانشجویی بازیابی کند. همچنین لیست دانشجوها بتواند در یک جدول
# نشان دهد و با انتخاب هر دانشجو (دانشجویان) آن دانشجو را حذف یا ویرایش کرد.

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


class add_studnet:

    def students_file(self, item):
        f = open('studentsName.txt', 'a')
        f.write(item + '\n')

    def addStudent(self, item):
        for i in range(item):
            print('please enter the new file name for keeping new information:')
            x = str(input('use the name of new student:') + '_student.txt')

            self.students_file(x)

            s = student()
            s.file_name(x)
            print('please enter the information of new student:')

            s.first_name(input('Name:'))
            s.last_name(input('LastName:'))
            s.father_name(input('FatherName:'))
            s.student_code(input('StudentCode:'))


saleh = add_studnet()
saleh.addStudent(2)
