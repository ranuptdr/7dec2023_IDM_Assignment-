# import module name
import sys #sys is a built-in module in python

# from top-level module.submodul import  element1,element2,........
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.QtGui import QIcon 

# classobject = ClassName()
# Creating an instance/object of QApplication
app = QApplication([]) # []passing am empty list, app is a external clas object
window = QWidget()  # win  is a external clas object,   Creating an instance of QWidget
window = QMainWindow()

# Setting the window title
window.setWindowTitle("Internet Download Manager 6.8")
iconCo = QIcon('./img.png')
window.setWindowIcon(iconCo)

# create a menubar
menu_bar = window.menuBar()
tasks_menu = menu_bar.addMenu('Tasks')
file_menu = menu_bar.addMenu("File")
downloads_menu = menu_bar.addMenu('Downloads')
view_menu = menu_bar.addMenu("View")
help_menu = menu_bar.addMenu("Help")
registration_menu = menu_bar.addMenu("Registration")

# classobject.method()
window.show() 
app.exec()