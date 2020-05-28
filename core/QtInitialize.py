from PyQt5.QtWidgets import QWidget
from UI import main_UI
from core import Word


class MainUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.main_ui = main_UI.Ui_Form()
        self.main_ui.setupUi(self)
        self.main_ui.name.textChanged.connect(self.get_texts)
        self.main_ui.ok.clicked.connect(self.save_word)

    def get_texts(self, name: str):
        word = Word.load(name)
        temp_ui = self.main_ui
        temp_ui.meanings.setText(word.get_all_meanings())
        temp_ui.origins.setText(word.get_all_origins())

    def save_word(self):
        temp_ui = self.main_ui
        name = temp_ui.name.text()
        if temp_ui.new_meaning.toPlainText() != '' and temp_ui.new_origin.toPlainText() != '' and Word.check(name):
            meaning = Word.Meaning(temp_ui.new_meaning.toPlainText(), temp_ui.new_origin.toPlainText())
            word = Word.Word(name, [meaning])
            Word.save(word)
            self.get_texts(name)
            temp_ui.new_meaning.setText('')
            temp_ui.new_origin.setText('')
