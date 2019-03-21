from flask import Flask, request, session, redirect, url_for, render_template, flash
from .models import search, add

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

@app.route('/')
def welcome():
    return render_template('index.html')
@app.route('/post', methods=['POST'])
def methodPost():
    word = request.form['word']
    return word
@app.route('/get')
def methodGet():
    word = request.args.get("word")
    return search(word)
@app.route('/add/<word>')
def like_post(word):
    # session_key = session.get('key')
    sc = request.args.get("sc")
    if add(word,sc):
        return "Fine"
    return "Not OK"
if __name__ == '__main__':
    app.run(host='0.0.0.0')
