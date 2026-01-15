from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Task

app = Flask(__name__)
app.config['SECRET_KEY'] = 'taskflow-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taskflow.db'

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

# ---------- AUTH ----------
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect('/dashboard')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed = generate_password_hash(request.form['password'])
        user = User(
            full_name=request.form['name'],
            email=request.form['email'],
            password=hashed
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

# ---------- DASHBOARD ----------
@app.route('/dashboard')
@login_required
def dashboard():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    completed = len([t for t in tasks if t.status == "Completed"])
    pending = len(tasks) - completed
    percent = int((completed / len(tasks)) * 100) if tasks else 0
    return render_template(
        'dashboard.html',
        total=len(tasks),
        completed=completed,
        pending=pending,
        percent=percent,
        tasks=tasks[:5]
    )

# ---------- TASKS ----------
@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    if request.method == 'POST':
        task = Task(
            title=request.form['title'],
            description=request.form['description'],
            priority=request.form['priority'],
            due_date=request.form['due_date'],
            user_id=current_user.id
        )
        db.session.add(task)
        db.session.commit()
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/task/<int:id>/toggle')
@login_required
def toggle_task(id):
    task = Task.query.get(id)
    task.status = "Completed" if task.status == "Pending" else "Pending"
    db.session.commit()
    return redirect('/tasks')

@app.route('/task/<int:id>/delete')
@login_required
def delete_task(id):
    db.session.delete(Task.query.get(id))
    db.session.commit()
    return redirect('/tasks')

# ---------- PROFILE ----------
@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
