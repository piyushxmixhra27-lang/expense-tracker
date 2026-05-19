import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expense.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='Pending')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    # Only drop and recreate in development to apply schema changes
    db.drop_all()
    db.create_all()
    # Create default admin user
    if not User.query.filter_by(username='admin@company.com').first():
        hashed_pw = bcrypt.generate_password_hash('password').decode('utf-8')
        admin = User(username='admin@company.com', password=hashed_pw, role='admin')
        db.session.add(admin)
        db.session.commit()

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = True if request.form.get('remember-me') else False
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=remember)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user_exists = User.query.filter_by(username=username).first()
        if user_exists:
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('register'))
            
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_pw, role='user')
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    total_expenses = sum(exp.amount for exp in expenses)
    monthly_budget = 5000.0 # Hardcoded for now
    remaining_budget = monthly_budget - total_expenses
    budget_percentage = (total_expenses / monthly_budget) * 100 if monthly_budget > 0 else 0
    
    # Recent activity
    recent_activity = Expense.query.filter_by(user_id=current_user.id).order_by(Expense.date.desc()).limit(5).all()
    
    return render_template('dashboard.html', 
                           total_expenses=total_expenses, 
                           remaining_budget=remaining_budget,
                           budget_percentage=budget_percentage,
                           recent_activity=recent_activity)

from datetime import datetime

@app.route('/add_expense', methods=['POST'])
@login_required
def add_expense():
    title = request.form.get('title')
    amount = request.form.get('amount')
    category = request.form.get('category')
    date_str = request.form.get('date')
    
    if title and amount and category and date_str:
        expense_date = datetime.strptime(date_str, '%Y-%m-%d')
        new_expense = Expense(
            title=title,
            amount=float(amount),
            category=category,
            date=expense_date,
            user_id=current_user.id,
            status='Approved'
        )
        db.session.add(new_expense)
        db.session.commit()
        flash('Expense added successfully!', 'success')
    else:
        flash('Please fill all fields', 'error')
        
    return redirect(request.referrer or url_for('dashboard'))

@app.route('/analytics')
@login_required
def analytics():
    return render_template('analatics.html')

@app.route('/budget')
@login_required
def budget():
    return render_template('budget.html')

@app.route('/reports')
@login_required
def reports():
    return render_template('reports.html')

@app.route('/transactions')
@login_required
def transactions():
    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    return render_template('transactions.html', expenses=expenses)

@app.route('/settings')
@login_required
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True)
