TaskFlow - Task Management Application

>> Project Overview

TaskFlow is a web-based task management application built with Flask and SQLAlchemy. It allows users to create accounts, authenticate securely, and manage their tasks efficiently. Users can organize tasks by priority, status, and due dates, with a clean and intuitive dashboard interface.

>> Key Features

- **User Authentication**: Secure login and registration system with password hashing
- **Task Management**: Create, view, and manage tasks with priority levels and status tracking
- **User Dashboard**: Personalized dashboard for each user to view their tasks
- **User Profile**: View and manage user account information
- **Responsive Design**: Clean, modern UI with CSS styling and JavaScript interactions

>> Technology Stack

- **Backend**: Python with Flask web framework
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Flask-Login with Werkzeug security
- **Database ORM**: Flask-SQLAlchemy

>> Project Structure

```
taskflow/
├── app.py                 # Main Flask application and routes
├── models.py              # Database models (User, Task)
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── templates/             # HTML templates
│   ├── base.html          # Base template with navigation
│   ├── login.html         # Login page
│   ├── register.html      # User registration page
│   ├── dashboard.html     # Main dashboard
│   ├── tasks.html         # Task management page
│   └── profile.html       # User profile page
└── static/                # Static files
    ├── css/
    │   └── style.css      # Application styling
    └── js/
        └── main.js        # Client-side JavaScript
```

---

>> Setup Instructions

### Step 1: Prerequisites Check

Ensure you have the following installed on your system:

- **Python 3.7 or higher**
- **pip** (Python package manager)
- **Git** (for version control)

To verify installations, run:

```bash
python --version
pip --version
git --version
```

### Step 2: Clone or Download the Project

If you haven't already, navigate to your project directory:

```bash
cd C:\Users\viren\OneDrive\Desktop\Task\ Flow
```

### Step 3: Create a Python Virtual Environment

Creating a virtual environment isolates project dependencies from system Python.

>> On Windows (PowerShell/CMD): 

```bash
python -m venv venv
```

 >> Activate the virtual environment: 

```bash
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows CMD
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

You should see `(venv)` appear in your terminal prompt when activated.

### Step 4: Install Project Dependencies

With the virtual environment activated, install all required Python packages:

```bash
pip install -r requirements.txt
```

This installs:

- **Flask** - Web framework
- **Flask-SQLAlchemy** - Database ORM
- **Flask-Login** - User session management
- **Werkzeug** - Security utilities for password hashing

Verify installation:

```bash
pip list
```

### Step 5: Initialize the Database

The application uses SQLite database. The database is automatically created when you first run the app, but you can pre-initialize it:

```bash
python -c "from app import app, db; app.app_context().push(); db.create_all(); print('Database initialized successfully')"
```

### Step 6: Run the Application

Start the Flask development server:

```bash
python app.py
```

You should see output like:

```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 7: Access the Application

Open your web browser and navigate to:

```
http://localhost:5000
```

---

>> Usage Guide

### First-Time Setup

1. Register a New Account

   - Click the "Register" button on the login page
   - Enter your full name, email, and password
   - Click "Register" to create your account

2. Login

   - Use your registered email and password
   - You'll be redirected to your dashboard

3. Create Tasks

   - Navigate to the "Tasks" page
   - Click "New Task" to create a task
   - Fill in title, description, priority, and due date
   - Click "Create Task" to save

4. Manage Tasks

   - View all your tasks on the dashboard
   - Update task status (Pending, In Progress, Completed)
   - Set priority levels (Low, Medium, High)
   - Delete tasks when no longer needed

5. View Profile
   - Click on "Profile" to see your account information
   - Update your details if needed

---

>> Environment Variables & Configuration

### Secret Key

The application uses a secret key for session management. In `app.py`:

```python
app.config['SECRET_KEY'] = 'taskflow-secret'
```

For production, change this to a secure, random string:

```bash
# Generate a secure key (run this in Python)
python -c "import secrets; print(secrets.token_hex(32))"
```

### Database Configuration

The application uses SQLite by default:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taskflow.db'
```

The database file `taskflow.db` will be created in your project root directory automatically.

---

>> Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"

**Solution**: Ensure your virtual environment is activated and dependencies are installed:

```bash
# Activate virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Issue: "Port 5000 is already in use"

>> Solution**: Change the port in `app.py`:

```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)
```

### Issue: Database locked or corrupted

 >> Solution**: Delete `taskflow.db` and restart the application:

```bash
rm taskflow.db  # Linux/macOS
del taskflow.db # Windows
python app.py
```

>> Issue: Git not found

-- Solution --: Install Git from https://git-scm.com/download/win and restart your terminal.

---

>> Development Workflow

>>> Making Changes

1. Modify code in your editor
2. Flask auto-reloads when debug mode is on
3. Test changes in your browser
4. Check console for errors

>> Deactivating Virtual Environment

When finished, deactivate the virtual environment:

```bash
deactivate
```

>> Version Control

Track your changes with Git:

```bash
git init
git add .
git commit -m "Initial TaskFlow setup"
```

---

>> Dependencies Details

| Package          | Version | Purpose                                    |
| ---------------- | ------- | ------------------------------------------ |
| Flask            | Latest  | Web framework for building the application |
| Flask-SQLAlchemy | Latest  | ORM for database operations                |
| Flask-Login      | Latest  | User session and authentication management |
| Werkzeug         | Latest  | Security utilities for password hashing    |

---

>> Support & Documentation

- **Flask Documentation**: https://flask.palletsprojects.com/
- **SQLAlchemy Documentation**: https://docs.sqlalchemy.org/
- **Flask-Login Documentation**: https://flask-login.readthedocs.io/

---

>> License

This project is open source and available under the MIT License.

---

> Author Notes

TaskFlow is designed for personal task management and can be extended with additional features such as:

- Task categories/tags
- Recurring tasks
- Task notifications
- Team collaboration
- Mobile app version

---

Last Updated**: January 15, 2026
