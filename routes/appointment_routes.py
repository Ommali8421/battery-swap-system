from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user

appointment_bp = Blueprint('appointment', __name__)

@appointment_bp.route('/book', methods=['GET', 'POST'])
@login_required
def book():
    cur = current_app.mysql.connection.cursor()

    if request.method == 'POST':
        station_id = request.form['station']
        appointment_time = request.form['appointment_time']

        # Insert into appointments
        cur.execute("""
            INSERT INTO appointments (user_id, station_id, appointment_time)
            VALUES (%s, %s, %s)
        """, (current_user.id, station_id, appointment_time))

        current_app.mysql.connection.commit()
        cur.close()

        flash("Appointment booked successfully!", "success")
        return redirect(url_for('user.dashboard'))

    # For GET: fetch all stations
    cur.execute("SELECT id, name FROM stations")
    stations = cur.fetchall()
    cur.close()

    return render_template('book.html', stations=stations)
