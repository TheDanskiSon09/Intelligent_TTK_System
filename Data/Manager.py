import json

import Container as con


class Saver():
    def __init__(self):
        print("Инициализация!")
    def LoadWords(self):
        return json.load(open("Data/Words.json", encoding='utf-8'))
    def SaveWords(self):
        with open('Data/Words.json', 'w', encoding='utf-8') as file:
            json.dump(con.Words, file, ensure_ascii=False, indent=2)
    def LoadMessages(self):
        return json.load(open("Data/Messages.json", encoding='utf-8'))
    def SaveMessages(self):
        with open('Data/Messages.json', 'w', encoding='utf-8') as file:
            json.dump(con.Messages, file, ensure_ascii=False, indent=2)
    def LoadUsers(self):
        return json.load(open("Data/Users.json", encoding='utf-8'))
    def SaveUsers(self):
        with open('Data/Users.json', 'w', encoding='utf-8') as file:
            json.dump(con.Users, file, ensure_ascii=False, indent=2)
    def LoadAdmins(self):
        return json.load(open("Data/Admins.json", encoding='utf-8'))
    def SaveAdmins(self):
        with open('Data/Admins.json', 'w', encoding='utf-8') as file:
            json.dump(con.Admins, file, ensure_ascii=False, indent=2)
    def LoadSettings(self):
        return json.load(open("Data/Settings.json", encoding='utf-8'))
    def SaveSettings(self):
        with open('Data/Settings.json', 'w', encoding='utf-8') as file:
            json.dump(con.Settings, file, ensure_ascii=False, indent=2)
