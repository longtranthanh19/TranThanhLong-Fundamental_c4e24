from flask import Flask, render_template, request
from models.bike import Bike
import mlab

mlab.connect()
app = Flask(__name__)

@app.route('/')
def home():
    return "Homee"

@app.route('/bike', methods=["GET", "POST"])
def new_bike():
    if request.method == "GET":
        return render_template("ex1.html")
    elif request.method == "POST":
        form = request.form
        model = form["model"]
        fee = form["fee"]
        image = form["image"]
        year = form["year"]
        new_bike = New_bike(model=model, 
                            fee=fee, 
                            image=image, 
                            year=year)
        new_bike.save()
        return "Success"

if __name__ == '__main__':
  app.run(debug=True)