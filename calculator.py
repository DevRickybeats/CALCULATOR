from flask import Flask, flash, redirect, render_template, request, url_for, request


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # required for flash()

@app.route('/')
def calculator():
    return render_template('calculator.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    operation = request.form.get('operation')
    
    if not num1 or not num2:
        flash('Please enter valid numbers.', 'danger')
        return redirect(url_for('calculator'))
    if not operation:
        flash('Please select an operation.', 'danger')
        return redirect(url_for('calculator'))
    if not num1.isdigit() or not num2.isdigit():
        flash('Please enter valid numbers.', 'danger')
        return redirect(url_for('calculator'))

    try:
        if operation == 'add':
            result = int(num1) + int(num2)
        elif operation == 'subtract':
            result = int(num1) - int(num2)
        elif operation == 'multiply':
            result = int(num1) * int(num2)
        else:
            if num2 == 0:
                flash('Cannot divide by zero.', 'danger')
                return redirect(url_for('calculator'))
            else:
                result = int(num1) / int(num2)
    except Exception as e:
        flash('An error occurred: {}'.format(e), 'danger')
        return redirect(url_for('calculator'))
    return render_template('calculator.html', result=result)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')       
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
