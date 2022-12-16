from flask import *
app= Flask(__name__)

@app.route('/')
def d():
    return render_template("lab.html")

if __name__=="__main__":
    app.run()
