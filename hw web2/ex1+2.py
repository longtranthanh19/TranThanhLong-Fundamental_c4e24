from flask import Flask,render_template,request   
import mlab 
from mongoengine import Document, StringField, IntField
mlab.connect()

class Users(Document):
  name = StringField()
  email = StringField()
  username = StringField()
  password = StringField()

app = Flask(__name__)

# @app.route('/register')
# def register():
#     return render_template("register.html")
@app.route("/")
def home():
  return ''

@app.route('/register',methods = ['POST', 'GET'])
def register():
   if request.method == 'GET':
      return render_template("register.html")
   elif request.method == 'POST':
      form = request.form
      name = form["name"]
      email = form["email"]
      username= form["username"]
      password = form["password"]

      u = Users(name=name,email=email,username=username,password=password)
      u.save()
      return "You Signed Up Successfully"


  

if __name__ == '__main__':
  app.run(debug=True)