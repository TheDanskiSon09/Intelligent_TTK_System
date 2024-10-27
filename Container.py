import Data.Manager as man
Saver = man.Saver()
Admins = Saver.LoadAdmins()
Words = Saver.LoadWords()
Messages = Saver.LoadMessages()
Users = Saver.LoadUsers()
Settings = Saver.LoadSettings()