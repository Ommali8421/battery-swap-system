from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user

admin_bp = Blueprint('admin', __name__)

#  Simple check for admin based on email
def is_admin():
    return current_user.email == "admin@example.com"

# Manage Charging Stations
@admin_bp.route('/admin/stations', methods=['GET', 'POST'])
@login_required
def manage_stations():
    if not is_admin():
        return "Unauthorized", 403

    cur = current_app.mysql.connection.cursor()

    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']

        cur.execute("INSERT INTO stations (name, location) VALUES (%s, %s)", (name, location))
        current_app.mysql.connection.commit()
        flash("New station added!", "success")

    cur.execute("SELECT * FROM stations")
    stations = cur.fetchall()
    cur.close()

    return render_template('admin_stations.html', stations=stations)

# Delete a station
@admin_bp.route('/admin/delete-station/<int:station_id>', methods=['POST'])
@login_required
def delete_station(station_id):
    if not is_admin():
        return "Unauthorized", 403

    cur = current_app.mysql.connection.cursor()
    cur.execute("DELETE FROM stations WHERE id = %s", (station_id,))
    current_app.mysql.connection.commit()
    cur.close()
    flash("Station deleted!", "success")
    return redirect(url_for('admin.manage_stations'))

#  Admin Dashboard 
@admin_bp.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not is_admin():
        return "Unauthorized", 403

    cur = current_app.mysql.connection.cursor()
    cur.execute("""
        SELECT 
            a.id, 
            u.username, 
            s.name AS station_name, 
            a.appointment_time, 
            a.status
        FROM appointments a
        JOIN users u ON a.user_id = u.id
        JOIN stations s ON a.station_id = s.id
        ORDER BY a.appointment_time DESC
    """)
    appointments = cur.fetchall()
    cur.close()

    return render_template('admin_dashboard.html', appointments=appointments)

#  Admin – Update Appointment Status
@admin_bp.route('/admin/update-status/<int:appointment_id>', methods=['POST'])
@login_required
def update_status(appointment_id):
    if not is_admin():
        return "Unauthorized", 403

    new_status = request.form['status']
    cur = current_app.mysql.connection.cursor()
    cur.execute("UPDATE appointments SET status = %s WHERE id = %s", (new_status, appointment_id))
    current_app.mysql.connection.commit()
    cur.close()

    flash("Appointment status updated!", "success")
    return redirect(url_for('admin.admin_dashboard'))

