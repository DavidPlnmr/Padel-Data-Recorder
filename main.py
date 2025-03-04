import sys
from PyQt5.QtWidgets import QApplication
from gui.gui1 import Gui
import os

# If datafolder exists
if not os.path.exists('data'):
    os.makedirs('data')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Gui()
    demo.show()
    sys.exit(app.exec_())