from flask import Flask,  request, render_template,redirect,request,url_for
import pymysql

app = Flask(__name__)
conn=pymysql.connect('localhost','root','','web')

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/addnews')
def addup():
    return render_template('addnews.html')


@app.route('/page2')
def pagepdate():
    with conn:
        cur=conn.cursor()
        cur.execute("select * from newspath order by id desc;")
        rows=cur.fetchall()
        return render_template('page2.html',datas=rows)



@app.route('/pagenew')
def shownew():
    with conn:
        cur=conn.cursor()
        cur.execute("select * from newsing ORDER BY id desc;")
        rows=cur.fetchall()
        return render_template('page3.html',datas=rows)

@app.route('/addnews')
def addnews():
    return render_template('addnews.html')

@app.route('/addnew')
def addnew():
    return render_template('addnew.html')

#@app.route("/delete/string:id_data>",methods=['GET'])
#def delete(id_data):
 #   with conn:
 #       cur=conn.cursor()
 #       cur.execute("delete from newsing where id=%s",(id_data))
 #       conn.comit()
 #   return render_template('page3.html')


@app.route('/insert',methods=['POST'])
def insert():
    if request.method=="POST":
        title=request.form['title']
        details=request.form['desc']
        url=request.form['url']
        with conn.cursor() as cursur:
            sql="INSERT INTO `newspath` (`title`, `details`,`url`) values(%s,%s,%s) "
            cursur.execute(sql,(title,details,url))
            conn.commit()
        return redirect(url_for('pagepdate'))

@app.route('/insertnew',methods=['POST'])
def insertnew():
    if request.method=="POST":
        title=request.form['title']
        details=request.form['desc']
        url=request.form['url']
        with conn.cursor() as cursur:
            sql="INSERT INTO `newsing` (`title`, `details`,`url`) values(%s,%s,%s)"
            cursur.execute(sql,(title,details,url))
            conn.commit()
        return redirect(url_for('shownew'))

if __name__ =="__main__":
    app.run(debug=True)