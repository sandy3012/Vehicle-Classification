from flask import Flask, render_template, request
from blueprints import *

app = Flask(__name__)

app.register_blueprint(homepage)
app.register_blueprint(classify)

if __name__ == '__main__':
    app.run(debug=True)