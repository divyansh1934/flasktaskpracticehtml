from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/calculate',methods=["POST","GET"])
def calculate():
     if request.method=='GET':
        return render_template('calculate.html')
     else:
        operation=str(request.form["operation"])
        number1=float(request.form["number1"])
        number2=float(request.form["number2"])
        result=0
        if operation=="add":
            result=number1+number2
        elif operation=="multiply":
            result=number1*number2
        elif operation=="division":
            result=number1/number2
        else:
            result=number1-number2
        
        return render_template('result.html',result=result)
        #return render_template('calculate.html', result=result)

if __name__=='__main__':
    app.run(debug=True)