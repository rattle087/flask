
from flask import Flask, redirect, url_for, request 
app = Flask(__name__) 
  
@app.route('/input',methods = ['POST','GET']) 
def input():       
    num1 = request.form['num1']
    num2 = request.form['num2']
    func = request.form['func']
    if func == 'A' :       
        return num1 + num2
    elif func == 'D':     
        return num1 / num2
    elif func == 'M':       
        return num1 * num2 
    elif func == 'S' :    
	    return num1 - num2 
  
if __name__ == '__main__': 
    app.run(debug = True)

