from flask import Flask, render_template

app = Flask(__name__)

# test route decorator
@app.route('/')
def welcome():
    #  return ("<h1>welcome</h1>")
    return render_template('index.html')

@app.route('/hola')
def hola():
    return ("<h1>Hello</h1>")

@app.route('/user/<name>')
def user(name):
    return ("<h1>Hello {} </h1>".format(name))

@app.errorhandler(404)
def page_not_found_400(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def page_not_found_500(e):
    return render_template("500.html"),500