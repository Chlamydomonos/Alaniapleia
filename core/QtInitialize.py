from PyQt5.QtWidgets import QWidget
from UI import main_UI
from core import Word


class MainUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.main_ui = main_UI.Ui_Form()
        self.main_ui.setupUi(self)
        self.main_ui.name.textChanged.connect(self.get_texts)

    def get_texts(self, name: str):
        word = Word.load(name)
        temp_ui = self.main_ui
        temp_ui.meanings.setText(word.get_all_meanings())
        temp_ui.origins.setText(word.get_all_origins())
