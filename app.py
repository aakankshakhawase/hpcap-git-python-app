from flask import Flask, request, render_template_string

app = Flask(__name__)

# Home route with name and roll number displayed
@app.route('/')
def home():
    name = "Aakanksha Khawase"
    roll_number = "240840141001"
    return render_template_string('''
        <center>
        <h1>Welcome to the Flask Calculator</h1>
        <p>Name: {{ name }}</p>
        <p>Roll Number: {{ roll_number }}</p>
        <form action="/calculate" method="post">
            <input type="text" name="num1" placeholder="Enter first number" required>
            <select name="operation">
                <option value="add">Add</option>
                <option value="subtract">Subtract</option>
                <option value="multiply">Multiply</option>
                <option value="divide">Divide</option>
            </select>
            <input type="text" name="num2" placeholder="Enter second number" required>
            <button type="submit">Calculate</button>
        </form>
        </center>
    ''', name=name, roll_number=roll_number)


# Route to perform the calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero"
        else:
            result = "Invalid operation"

        return render_template_string('''
            <center>
            <h1>Welcome to the Flask Calculator</h1>
            <p>Name: {{ name }}</p>
            <p>Roll Number: {{ roll_number }}</p>
            <p>Result: {{ result }}</p>
            <a href="/">Back to Home</a>
            </center>
        ''', name="Aakanksha Khawase", roll_number="240840141001", result=result)
    
    except ValueError:
        return "Error! Please enter valid numbers."


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

