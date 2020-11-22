from flask import Flask, render_template
import datetime
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
sou
# 定义movie路径，当用户访问ip/movie时返回movie.html
@app.route('/movie')
def moive():
    # 列表用来存储执行获得的数据
    datalist = []
    conn = sqlite3.connect('movie.db')

    cursor = conn.cursor()

    sql = 'select * from movie250 limit 10'
    data = cursor.execute(sql)
    for item in data:
        datalist.append(item)
        # 功能：连接数据库，拿到数据。
    cursor.close()
    conn.close()

    return render_template("movie.html", movie=datalist) # datalist赋值给movie传给html文件


@app.route('/score')
def score():
    score = []
    num = []
    con = sqlite3.connect('movie.db')
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])
    cur.close()
    con.close()

    return render_template("score.html", score = score, num = num)

@app.route('/word')
def word():
    return render_template("word.html")

@app.route('/team')
def team():
    return render_template("team.html")


if __name__ == "__main__":
    app.run(debug=True)
