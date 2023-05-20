from kivy import utils
from kivy.properties import NumericProperty, StringProperty
from kivymd.app import MDApp
from kivy.core.window import Window
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

    def build(self):
        pass

    def student(self, clas, idd):
        if clas == "":
            toast("Enter class")

        elif idd == "":
            toast("Enter ID")

        else:
            self.search_student(clas, idd)

    def search_student(self, clas, idd):
        data = TR.check_student(TR(), clas, idd)
        if data == "No":
            toast("Invalid id")

        elif data == "Noclass":
            toast("Invalid Class")

        else:
            self.name = data["Name"]
            self.screen_capture("info")

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
