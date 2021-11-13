#Add two numbers
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')

def hello():
    return "<h1>hello</h1>"

@app.route('/add/<int:a>,<int:b>',methods=['GET'])
def add(a,b):
    ans=a+b
    ans2=str(ans)
    #return jsonify({'Sum': ans})
    return ans2
if __name__  == "__main__":    

 app.run(debug=True)
