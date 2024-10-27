import json

from flask import Flask, render_template, request, jsonify, make_response
from pymystem3 import Mystem

import Container as con

def Start():
  app = Flask(__name__)
  mystem = Mystem()
  @app.route('/')
  def index():

    return render_template('index.html')
  @app.route('/login')
  def LoginPage():

    return render_template('login.html')

  @app.route('/adduser', methods=['POST'])
  def AddUser():
    name = request.cookies["Login"]
    password = request.cookies['Password']
    if name in con.Admins.keys() and password == con.Admins[name]['password'] and con.Admins[name]['admin'] == True:
      login = request.form['login']
      password = request.form['password']
      IsAdmin = request.form['admin']
      if IsAdmin == "true":
        IsAdmin = True
      else:
        IsAdmin = False
      con.Admins[login] = {"password": password, "admin": IsAdmin}
      con.Saver.SaveAdmins()
      return jsonify({"message": True})
    return jsonify({"message": False})
  @app.route('/remuser', methods=['POST'])
  def RemUser():
    name = request.cookies["Login"]
    password = request.cookies['Password']
    if name in con.Admins.keys() and password == con.Admins[name]['password'] and con.Admins[name]['admin'] == True and name != request.form['name']:
      name = request.form['name']
      del con.Admins[name]
      con.Saver.SaveAdmins()
      return jsonify({"message": True})
    return jsonify({"message": False})
  @app.route('/loginSend', methods=['POST'])
  def Login():
    name = request.form['login']
    password = request.form['password']
    if name in con.Admins and password == con.Admins[name]["password"]:
      response = make_response(jsonify({"message": True}))
      response.set_cookie('Login', name, expires=0, max_age=3600)
      response.set_cookie('Password', password, expires=0, max_age=3600)
      return response
    else:
      return jsonify({"message": False})
  @app.route('/Isadmin', methods=['GET'])
  def IsAdmin():
    if "Login" in request.cookies and "Password" in request.cookies:
      name = request.cookies["Login"]
      password = request.cookies["Password"]
      if name in con.Admins and password == con.Admins[name]["password"]:
        return jsonify({"message": con.Admins[name]["admin"]})

  @app.route('/getusers', methods=['GET'])
  def GetUsers():
    if "Login" in request.cookies and "Password" in request.cookies:
      name = request.cookies["Login"]
      password = request.cookies["Password"]
      if name in con.Admins and password == con.Admins[name]["password"]:
        users = list(con.Admins.keys())
        print(users)
        return jsonify({"users": users})
  @app.route('/Islogined', methods=['GET'])
  def IsLogined():
    if "Login" in request.cookies and "Password" in request.cookies:
      name = request.cookies["Login"]
      password = request.cookies["Password"]
      if name in con.Admins and password == con.Admins[name]["password"]:
        return jsonify({"message": True})
      else:
        return jsonify({"message": False})
    else:
      return jsonify({"message": False})

  @app.route('/send', methods=['POST'])
  def Send():
    if "Login" in request.cookies and "Password" in request.cookies:
      name = request.cookies["Login"]
      password = request.cookies["Password"]
      if name in con.Admins and password == con.Admins[name]["password"]:
        words = json.loads(request.form['words'])
        messages = json.loads(request.form['messages'])
        con.Messages = messages
        con.Saver.SaveMessages()
        unique_lemmatized_words = {}
        for i in words.keys():
          text = ' '.join(words[i])

          # Лемматизация всего текста
          lemmatized_words = mystem.lemmatize(text)

          # Убираем пустые строки и сохраняем только уникальные леммы с помощью множества
          unique_lemmatized_words[i] = set(word for word in lemmatized_words if word.strip())

          # Преобразуем обратно в список, если необходимо
          unique_lemmatized_words[i] = list(unique_lemmatized_words[i])
        con.Words = unique_lemmatized_words
        con.Saver.SaveWords()
        print(con.Words)
        return jsonify({"message": "text"})
  @app.route('/getdata', methods=['GET'])
  def GetWords():
    if "Login" in request.cookies and "Password" in request.cookies:
      name = request.cookies["Login"]
      password = request.cookies["Password"]
      if name in con.Admins and password == con.Admins[name]["password"]:
        return jsonify({"words": con.Words, "messages": con.Messages})
  app.run(debug=False, host="192.168.31.213")