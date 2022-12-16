from flask import *

app = Flask(__name__)


@app.route("/student/<student_id>")
def student_details(student_id):
    return f"you are viewing the details of {student_id}"


@app.route("/")
def main():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
