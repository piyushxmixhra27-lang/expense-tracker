from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/analytics')
def analytics():
    return render_template('analatics.html')

@app.route('/budget')
def budget():
    return render_template('budget.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/transactions')
def transactions():
    return render_template('transactions.html')

if __name__ == '__main__':
    app.run(debug=True)
