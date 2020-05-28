import pickle
import os.path


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

    def get_all_meanings(self):
        temp = ''
        for i in range(len(self.meanings)):
            temp += str(i+1)
            temp += '.'
            temp += self.meanings[i].meaning
            temp += '\n'
        return temp

    def get_all_origins(self):
        temp = ''
        for i in range(len(self.meanings)):
            temp += str(i+1)
            temp += '.'
            temp += self.meanings[i].origin
            temp += '\n'
        return temp


def save(word: Word):
    path = 'data\\' + word.name + '.word'
    if os.path.isfile(path):
        f = open(path, 'rb')
        temp_word = pickle.load(f)
        f.close()
        f = open(path, 'wb')
        pickle.dump(temp_word + word, f)
        f.close()
    else:
        f = open(path, 'wb+')
        pickle.dump(word, f)
        f.close()


def load(name: str):
    empty_word = Word('-', [Meaning('-', '-')])
    path = 'data\\' + name + '.word'
    if os.path.isfile(path):
        f = open(path, 'rb')
        return pickle.load(f)
    else:
        return empty_word


def check(word: str):
    for i in range(len(word)):
        if i == 0:
            return True
    return True
