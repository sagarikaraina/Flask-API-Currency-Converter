from flask import Flask,request ,render_template , jsonify

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')
    
@app.route('/calculate',methods=['POST'])
def rates():
    if(request.method == 'POST'):
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = int(request.form['num1'])
    exchange_rates = {
        "USD": {"EUR": 0.94, "GBP": 0.83, "INR": 82.61},
        "EUR": {"USD": 1.06, "GBP": 0.88, "INR": 87.55},
        "GBP": {"USD": 1.21, "EUR": 1.14, "INR": 99.86},
        "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.010}
    }
    rate = exchange_rates[from_currency][to_currency]
    converted_amount = amount * rate
    result=str(amount)+" "+str(from_currency) +" = "+ str(converted_amount) +" "+str(to_currency)
    return render_template('results.html' , result = result)

@app.route('/postman_action',methods=['POST'])
def currency_conversion_api():
    if(request.method == 'POST'):
        from_currency = request.json['from_currency']
        to_currency = request.json['to_currency']
        amount = int(request.json['num1'])
    exchange_rates = {
        "USD": {"EUR": 0.94, "GBP": 0.83, "INR": 82.61},
        "EUR": {"USD": 1.06, "GBP": 0.88, "INR": 87.55},
        "GBP": {"USD": 1.21, "EUR": 1.14, "INR": 99.86},
        "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.010}
    }
    rate = exchange_rates[from_currency][to_currency]
    converted_amount = amount * rate
    result=str(amount)+" "+str(from_currency) +" = "+ str(converted_amount) +" "+str(to_currency)
    return jsonify(result)

if __name__=="__main__":
    app.run(host="0.0.0.0")

