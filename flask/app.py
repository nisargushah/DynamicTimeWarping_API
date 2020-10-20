from flask import Flask, render_template
#from algorithm.dwtBaseCode import *
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/nisargshah/Desktop/Research/DynamicTimeWarping_API/algorithm')
from dtwBaseCode import main

import dtwBaseCode
app = Flask(__name__)

@app.route("/")
def hello():
    x = dtwBaseCode.main(sys.argv[1],sys.argv[2])
    return render_template('index.html', variable=x)



if __name__ == '__main__':
    app.run(debug = True )