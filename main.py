import fileinput
import os
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('پروژه درس مباحث ویژه')


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

    def addStudent(self, item, in1, in2, in3, in4):
        for i in range(item):
            x = str(in4 + '_student.txt')

            self.students_file(x)

            s = student()
            s.file_name(x)

            s.first_name(in1)
            s.last_name(in2)
            s.father_name(in3)
            s.student_code(in4)

    def removeStudnet(self, item):

        if os.path.exists(item):
            os.remove(item)
            messagebox.showinfo('Error', 'دانشجو حذف شد')
        else:
            messagebox.showerror('Error', 'دانشجویی با این مشخصات وجود ندارد')

    def changeStudent(self, item, inp1, inp2):

        textToSearch = inp1
        textToReplace = inp2

        fileToSearch = item

        tempFile = open(fileToSearch, 'r+')

        for line in fileinput.input(fileToSearch):
            tempFile.write(line.replace(textToSearch, textToReplace))

        tempFile.close()

    def showStudents(self):
        top = Toplevel()
        f = open('students_codes.txt', 'r')
        Label(top, text = 'first name').grid(row=0, column=0)
        Label(top, text = 'last name').grid(row=0, column=1)
        Label(top, text = 'student code').grid(row=0, column=2)
        r =1
        c =0
        for line in f:
            print(line[:21])
            newf = open(line[:21],'r')
            for i in newf:
                
                if i[:9] == 'FirstName':
                    Label(top, text = i[10:]).grid(row=r, column=c)
                elif i[:8] == 'LastName':
                    Label(top, text = i[9:]).grid(row=r, column=c+1)
                elif i[:11] == 'StudentCode':
                    Label(top, text = i[12:]).grid(row=r, column=c+2)
            r += 1

master = manipulating_studnet()


def add(top, in1, in2, in3, in4):
    firstName = in1.get()
    lastName = in2.get()
    fatherName = in3.get()
    studentId = in4.get()

    master.addStudent(1, firstName, lastName, fatherName, studentId)


def window_for_add():
    top = Toplevel()

    label1 = Label(top, text='first name:').grid(row=0, column=0)
    label2 = Label(top, text='last name:').grid(row=1, column=0)
    label3 = Label(top, text='father name:').grid(row=2, column=0)
    label4 = Label(top, text='student id:').grid(row=3, column=0)

    entry_field1 = Entry(top, width=50, borderwidth=5, fg='blue')
    entry_field1.grid(row=0, column=1)
    entry_field2 = Entry(top, width=50, borderwidth=5, fg='blue')
    entry_field2.grid(row=1, column=1)
    entry_field3 = Entry(top, width=50, borderwidth=5, fg='blue')
    entry_field3.grid(row=2, column=1)
    entry_field4 = Entry(top, width=50, borderwidth=5, fg='blue')
    entry_field4.grid(row=3, column=1)

    cancel_button = Button(top, text='Cancel', command=top.destroy).grid(row=4, column=0)
    exit_button = Button(top, text='Exit', command=top.quit).grid(row=4, column=2)
    sub_button = Button(top, text='seve',
                        command=lambda: add(top, entry_field1, entry_field2, entry_field3, entry_field4)).grid(row=4,
                                                                                                               column=1)


def remove(inp):
    master.removeStudnet('{}_student.txt'.format(inp.get()))


def window_for_remove():
    top = Toplevel()
    label1 = Label(top, text='Enter the student id to remove: ').grid(row=0, column=0)
    entry_field = Entry(top, width=50, borderwidth=5, fg='blue')
    entry_field.grid(row=1, column=0, columnspan=4)
    remove_button = Button(top, text='remove', command=lambda: remove(entry_field))
    remove_button.grid(row=2, column=0)
    cancel_button = Button(top, text='Cancel', command=top.destroy).grid(row=2, column=1)
    exit_button = Button(top, text='Exit', command=top.quit).grid(row=2, column=3)


def change(in1, in2, in3):
    master.changeStudent('{}_student.txt'.format(in1.get()), in2.get(), in3.get())


def window_for_change():
    top = Toplevel()
    label1 = Label(top, text='Enter the student id: ').grid(row=0, column=0)
    label2 = Label(top, text='Enter the thing you want to change: ').grid(row=1, column=0)
    label3 = Label(top, text='Enter the thing you want to replace: ').grid(row=2, column=0)
    entry_field1 = Entry(top, width=50, borderwidth=5, fg='blue')
    entry_field1.grid(row=0, column=1)
    entry_field2 = Entry(top, width=50, borderwidth=5, fg='blue')
    entry_field2.grid(row=1, column=1)
    entry_field3 = Entry(top, width=50, borderwidth=5, fg='blue')
    entry_field3.grid(row=2, column=1)
    submit = Button(top, text='save', command=lambda: change(entry_field1, entry_field2, entry_field3)).grid(row=3,
                                                                                                             column=0)
    cancel_button = Button(top, text='Cancel', command=top.destroy).grid(row=3, column=1)
    exit_button = Button(top, text='Exit', command=top.quit).grid(row=3, column=2)


def list_of_students():
    master.showStudents()


button1 = Button(root, text='اضافه کردن دانشجوری جدید', command=window_for_add)
button2 = Button(root, text='لیست دانشجویان', command=list_of_students)
button3 = Button(root, text='حذف دانشجو', command=window_for_remove)
button4 = Button(root, text='ویرایش دانشجو', command=window_for_change)

button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()
