import  Container as con
from pymystem3 import Mystem
m = Mystem()

def Init():
    global m
    m = Mystem()
def GetStandartWords(text:str):
    words = set(m.lemmatize(text))
    words.discard('\n')
    return words  # Преобразуем в множество
def FindWords(text:str):
    # Лемматизируем текст и преобразуем в множество
    standard_words = GetStandartWords(text)
    # Проверяем пересечение
    for i in con.Words.keys():
        print(standard_words)
        print(con.Words[i])
        if not standard_words.isdisjoint(con.Words[i]):
            if i in con.Messages:
                return con.Messages[i]
            else:
                return con.Settings["NotInMessage"]
    return con.Settings["NotInCategory"]
