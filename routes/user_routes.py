from flask import Blueprint, render_template, current_app
from flask_login import login_required, current_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/dashboard')
@login_required
def dashboard():
    cur = current_app.mysql.connection.cursor()
    cur.execute("""
        SELECT a.id, s.name AS station_name, a.appointment_time, a.status
        FROM appointments a
        JOIN stations s ON a.station_id = s.id
        WHERE a.user_id = %s
        ORDER BY a.appointment_time DESC
    """, (current_user.id,))
    
    appointments = cur.fetchall()
    cur.close()

    return render_template('dashboard.html', appointments=appointments)
