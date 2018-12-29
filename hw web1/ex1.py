from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/about-me")
def abm():
    i = {
        "Name":"Tran Thanh Long",
        "Work":"Student",
        "School":"USTH",
        "Hobbies":"Many things"
    }
    return render_template("about-me.html",
                            info = i )

 
@app.route("/school")
def school():
    return redirect("http://techkids.vn")

if __name__ == "__main__":
    app.run(debug=True)
