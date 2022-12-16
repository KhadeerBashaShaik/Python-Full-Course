import sqlite3
from flask import *

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('feedback.html')

@app.route("/success",methods=["POST", "GET"])  # type: ignore
def suc():
    msg='msg'
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            skill = request.form["skill"]
            with sqlite3.connect("feedback.db") as con:
                cur = con.cursor()
                cur.execute("create table feedback(name text,email text,skill text)")
                cur.execute("INSERT into feedback (name, email, skill) values (?,?,?)",
                            (name, email, skill))
                con.commit()
                msg = "Feedback successfully Added"
        except:
            con.rollback()
            msg = "We can not add the Feedback to the list"
        finally:
            con.close()
            return render_template("feed_s.html", msg=msg)
            
@app.route("/display")
def dis1():
    con = sqlite3.connect("feedback.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from feedback")
    rows = cur.fetchall()
    return render_template("delete_record.html",msg=rows )

if __name__ == '__main__':
    app.run(debug=True)
