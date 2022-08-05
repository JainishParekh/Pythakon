from flask import Flask,redirect,url_for,render_template,jsonify,request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.todos

@app.route('/index', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)

@app.route('/' )
def home():
    return render_template('home.html')

@app.route('/blog/<name>' , methods= ('GET' , 'POST'))
def blog():
    return render_template('blog.html')

@app.route('/videos' , methods= ('GET' , 'POST'))
def video():
    return render_template('videos.html')

@app.route('/about',methods = ('GET','POST'))
def about():
    return render_template('about.html')

@app.route('/contact',methods = ('GET','POST'))
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)