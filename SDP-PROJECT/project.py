from flask import Flask,render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('login.html')


@app.route("/index", methods=["POST", "GET"])  # type: ignore
def afterLogin():
    if request.method == "POST":
        a = request.form["userid"]
        b = request.form["pwd"]
        if a == "admin" and b == "admin":
            return render_template("index.html")
        else:
            return render_template("LoginFail.html")


@app.route("/input", methods=["POST", "GET"])
def liveUpdate():
    return render_template('input_for_live.html')


@app.route("/blog", methods=["POST", "GET"])
def blog():
    return render_template('blog.html')


@app.route("/news", methods=["POST", "GET"])
def news():
    url = "https://economictimes.indiatimes.com/markets/stocks/live-blog/bse-sensex-today-live-nifty-stock-market-updates-12-september-2022/liveblog/94140254.cms"
    req = requests.get(url)
    b = BeautifulSoup(req.content, 'html.parser')
    div_tag = b.findAll(attrs={'class': 'blogSysn'})
    with open('sample.txt', 'w') as f:
        for div in div_tag:
            f.write(" ".join(div.text.split()[1:]))
    with open('sample.txt', 'r') as f:
        r = f.read()
    return render_template('news.html', msg=r)


@app.route('/buy', methods=["POST", "GET"])
def buy_st():
    return render_template('buy.html')


@app.route("/about", methods=["POST", "GET"])
def about():
    return render_template('about.html')


@app.route("/live", methods=["POST", "GET"])  # type: ignore
def live():
    if request.method == "POST":
        a = request.form["st_input"]
        url = "https://www.screener.in/company/" + a
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        sp = soup.find_all('span')[1]
        price = str(sp.string)
        msg = price.replace("₹ ", "")
        return render_template("live.html", msg=msg, name_st=a)
    return None

if __name__ == '__main__':
    app.run()
