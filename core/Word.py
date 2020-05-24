class Meaning:
    def __init__(self, meaning: str, origin: str):
        self.meaning = meaning
        self.origin = origin


class Word:
    def __init__(self, name: str, meanings: list):
        self.name = name
        self.meanings = meanings

    def __add__(self, other):
        return Word(self.name, self.meanings + other.meanings)

    def meanings_amount(self):
        return len(self.meanings)

    def get_meaning(self, index: int):
        return self.meanings[index].meaning, self.meanings[index].origin
