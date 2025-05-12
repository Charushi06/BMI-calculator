from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    bmi = round(weight / ((height / 100) ** 2), 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    with open('results.txt', 'a') as file:
        file.write(f"{datetime.now()}, {name}, {weight}kg, {height}cm, BMI: {bmi} ({category})\n")

    return f"<h2>Thank you, {name}! Your BMI is {bmi} ({category})</h2><a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True)
