import os

from kivy import utils
from kivy.properties import NumericProperty, StringProperty
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase

from database import Transfer as TR

if utils.platform != 'android':
    Window.size = [360, 640]


class Tab(MDBoxLayout, MDTabsBase):
    pass


class MainApp(MDApp):
    # APP
    screens = ['entrance']
    screens_size = NumericProperty(len(screens) - 1)
    current = StringProperty(screens[len(screens) - 1])

    # student
    name = StringProperty("")
    work = StringProperty("")
    attend = StringProperty("")

    class_name = StringProperty("")
    read = StringProperty("")

    student_id = StringProperty("")
    readid = StringProperty("")

    class_save = StringProperty("")
    id_save = StringProperty("")

    # result
    math = StringProperty("")
    eng = StringProperty("")
    geo = StringProperty("")
    hist = StringProperty("")
    science = StringProperty("")

    def build(self):
        pass

    def on_start(self):
        Clock.schedule_once(lambda x: self.register_check(), .1)

    def student(self, clas, idd):
        if clas == "":
            toast("Enter class")

        elif idd == "":
            toast("Enter ID")

        else:
            self.search_student(clas, idd)

    def search_student(self, clas, idd):
        data = TR.check_student(TR(), clas, idd)
        if data == "Noclass":
            toast("Invalid Class")

        elif data == "No":
            toast("Invalid id")

        else:
            self.name = data["Name"]
            self.screen_capture("info")
            self.save_class(clas)
            self.save_id(idd)

    def homework(self):
        self.work = TR.fetch_homework(TR(), self.class_name)

    def result(self):
        data = TR.fetch_result(TR(), self.class_name, self.student_id)
        if data:
            self.math = data["Math"]
            self.eng = data["English"]
            self.geo = data["Geography"]
            self.hist = data["History"]
            self.science = data["Science"]

    def attendance(self):
        data = TR.get_attendance(TR(), self.class_name, self.student_id)
        if data == "present":
            self.attend = "Present"

        elif data == "absent":
            self.attend = "Absent"

    def save_class(self, name):
        with open("info.txt", "a") as fl:
            fl.write(name + '\n')
            self.class_name = name
        fl.close()

    def save_id(self, idd):
        with open("info.txt", "a") as fl:
            fl.write(idd)
            self.student_id = idd
        fl.close()

    def register_check(self):
        sm = self.root
        file_size = os.path.getsize("info.txt")
        if file_size == 0:
            pass
        else:
            sm.current = "info"
            self.readf()

    def readf(self):
        with open("info.txt", "r") as fl:
            read = fl.readlines()
            self.read = read[0].strip()
            self.readid = read[1].strip()
            self.class_name = self.read
            self.student_id = self.readid

            data = TR.check_student(TR(), self.class_name, self.student_id)
            self.name = data["Name"]

            self.attendance()
            self.homework()
            self.result()

        fl.close()

    def screen_capture(self, screen):
        sm = self.root
        sm.current = screen
        if screen in self.screens:
            pass
        else:
            self.screens.append(screen)
        print(self.screens)
        self.screens_size = len(self.screens) - 1
        self.current = self.screens[len(self.screens) - 1]
        print(f'size {self.screens_size}')
        print(f'current screen {screen}')


MainApp().run()
