from flask import *

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('login.html')


@app.route("/index", methods=["POST", "GET"])
def afterLogin():
    if request.method == "POST": 
        a = request.form["userid"]
        b = request.form["pwd"]
        if(a=="admin" and b=="admin"):
            return render_template("index.html")
        else:
            return render_template("LoginFail.html")



if __name__ == '__main__':
    app.run()
