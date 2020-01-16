from flask import Flask
from flask import render_template
import os

# Import local modules
from scripts.stress1 import create_bucket_f1
from scripts.stress2 import create_bucket_f2
from scripts.stress3 import create_bucket_f3
from scripts.stress4 import create_bucket_f4

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
        return render_template('error.html')

@app.route('/f1', methods=['GET'])
def f1():
        create_bucket_f1()
        return 'ok'

@app.route('/f2', methods=['GET'])
def f2():
        create_bucket_f2()
        return 'ok'

@app.route('/f3', methods=['GET'])
def f3():
        create_bucket_f3()
        return 'ok'

@app.route('/f4', methods=['GET'])
def f4():
        create_bucket_f4()
        return 'ok'

@app.route('/f5', methods=['GET'])
def f5():
        return 'ok'

@app.route('/f6', methods=['GET'])
def f6():
        return 'ok'

@app.route('/f7', methods=['GET'])
def f7():
        return 'ok'

@app.route('/f8', methods=['GET'])
def f8():
        return 'ok'

if __name__ == "__main__":
        app.run(debug=True,host='0.0.0.0', port=8080)
