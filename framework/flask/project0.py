# flask hello world web app
from flask import Flask

# create an instance of the Flask class.
app = Flask(__name__)

# decorator wrap functions into app.route function


@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello World"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9000)
