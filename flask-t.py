from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/wcc/')
@app.route('/wcc/<name>')
def hello(name=None):
    if name == None:
        return render_template('wcc1.html', name=name)
    else:
        return render_template(name, name=name)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')