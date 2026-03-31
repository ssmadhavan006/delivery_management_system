from flask import Flask, render_template, request, redirect, session
from db import get_db

app = Flask(__name__)
app.secret_key = "secret"   # needed for session

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email, password)
    )
    user = cursor.fetchone()
    
    if user:
        session['user'] = email   # store logged-in user
        return redirect('/dashboard')
    
    return "Invalid login"


@app.route('/dashboard')
def dashboard():
    # protect route
    if 'user' not in session:
        return redirect('/')
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    
    return render_template('dashboard.html', orders=orders)


@app.route('/create_order', methods=['POST'])
def create_order():
    if 'user' not in session:
        return redirect('/')
    
    address = request.form['address']
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO orders (address, status) VALUES (%s, %s)",
        (address, 'Pending')
    )
    db.commit()
    
    return redirect('/dashboard')


@app.route('/update_status/<int:id>')
def update_status(id):
    if 'user' not in session:
        return redirect('/')
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "UPDATE orders SET status='Delivered' WHERE id=%s",
        (id,)
    )
    db.commit()
    
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)