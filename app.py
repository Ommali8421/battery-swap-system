from flask import Flask, redirect, url_for
from flask_mysqldb import MySQL
from flask_login import LoginManager, current_user
from dotenv import load_dotenv
import os

# 🌐 Load environment variables
load_dotenv()

# 🔧 Initialize Flask app
app = Flask(__name__)

# ⚙️ Configurations
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MYSQL_HOST'] = os.getenv('DB_HOST')
app.config['MYSQL_USER'] = os.getenv('DB_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('DB_NAME')
app.config['MYSQL_PORT'] = int(os.getenv('DB_PORT', 3306))

# 🔌 Initialize and attach MySQL
mysql = MySQL(app)
app.mysql = mysql  # ✅ So current_app.mysql works in all routes

# 🔐 Setup LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# 📦 Register Blueprints
from routes.auth_routes import auth_bp
app.register_blueprint(auth_bp)

from routes.user_routes import user_bp
app.register_blueprint(user_bp)

from routes.appointment_routes import appointment_bp
app.register_blueprint(appointment_bp)

from routes.admin_routes import admin_bp
app.register_blueprint(admin_bp)

# 👤 User loader for Flask-Login
from models.user import User
@login_manager.user_loader
def load_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user_data = cur.fetchone()
    cur.close()
    if user_data:
        return User(user_data)
    return None

# 🏠 Redirect root URL
@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('user.dashboard'))
    return redirect(url_for('auth.login'))

# 🧪 Optional Test Route
@app.route('/test-db')
def test_db():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM stations;")
        rows = cur.fetchall()
        cur.close()
        return {'status': 'success', 'data': rows}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

# 🚀 Start the server
if __name__ == '__main__':
    try:
        print("🚀 Flask server is starting...")
        app.run(debug=True)
    except Exception as e:
        print("❌ Error starting server:", e)
