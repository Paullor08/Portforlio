from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def index_page(): 
    return render_template("welcome.html")

@app.route("/home")
def Home_page():
    return render_template("home.html")

@app.route("/profile")
def Personal_Profile_page():
    return render_template("profile.html")

@app.route("/education")
def Education_page():
    return render_template("education.html")

@app.route("/activity")
def Activity_page():
    return render_template("education.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)