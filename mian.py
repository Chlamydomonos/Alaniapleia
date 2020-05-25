import sys
from PyQt5.QtWidgets import QApplication
from core import QtInitialize


app = QApplication(sys.argv)
main_ui = QtInitialize.MainUI()

if __name__ == '__main__':
    main_ui.show()
    sys.exit(app.exec_())
