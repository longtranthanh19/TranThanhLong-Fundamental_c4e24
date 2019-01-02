from flask import Flask,render_template
app = Flask(__name__)

@app.route('/user/<username>')
def user_profile(username):
    users = {
        "Long" : {
                "name" : "Long",
                "age" : 18
        },
        "Duc" : {
                    "name" : "Duc",
                    "age" : 21
        }
    }
    return render_template("user_profile.html", users=users, username=username)

  

if __name__ == '__main__':
  app.run(debug=True)