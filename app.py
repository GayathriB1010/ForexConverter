from flask import Flask, request, render_template,flash,redirect
from forex_python.converter import CurrencyRates,CurrencyCodes,RatesNotAvailableError


app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/result',methods=["POST"])
def convert_currencies():
    try:
        amount = float(request.form['amount'])
    except ValueError:
        flash("Enter a valid amount")
        return redirect("/forex_form")
    try:
        convertFrom = request.form['convertFrom']
        convertTo = request.form['convertTo']
        if convertFrom == "" or convertTo == "":
            flash("Currencies cannot be empty")
            return redirect("/forex_form")
        c= CurrencyRates(force_decimal=False)
        cc = CurrencyCodes()
        result = c.convert(convertFrom,convertTo,amount)
        symbol = cc.get_symbol(convertTo)
        if symbol == None:
            flash("Enter a valid currency")
            return redirect("/forex_form")
        else:
            return render_template('result.html',result=result,symbol=symbol)       
    except RatesNotAvailableError:
        flash("Enter a valid currency")
        return redirect("/forex_form")

@app.route('/forex_form')
def forex_form():
    return render_template("forex_form.html")
        


