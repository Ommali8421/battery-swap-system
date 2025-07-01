
# 🔋 Battery Swap Appointment Booking System

A modern and user-friendly web application for booking electric vehicle battery swaps.  
Built using **Flask**, **MySQL**, and **Tailwind CSS**.

---

## 🚀 Features

- 🔐 User Registration & Login  
- 📅 Book Appointments at Charging Stations  
- 📋 User Dashboard to Track Appointments  
- ⚙️ Admin Panel to Manage Stations & Bookings  
- ✅ Appointment Status Update (Pending / Completed / Cancelled)

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python), Flask-Login  
- **Database**: MySQL  
- **Frontend**: HTML, Jinja2, Tailwind CSS  
- **Environment Management**: dotenv  
- **Version Control**: Git + GitHub

---

## 📂 Project Structure


battery-swap-system/
│
├── app.py                      # Main Flask application
├── .env                        # Environment variables
├── schema.sql                  # MySQL DB schema
├── requirements.txt            # Dependencies
│
├── models/
│   └── user.py                 # User class for Flask-Login
│
├── routes/
│   ├── auth\_routes.py          # Login/Register/Logout
│   ├── user\_routes.py          # Dashboard route
│   ├── appointment\_routes.py   # Appointment booking
│   └── admin\_routes.py         # Admin dashboard & station mgmt
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── book.html
│   ├── admin\_dashboard.html
│   └── admin\_stations.html
│
└── static/
├── css/styles.css
└── js/scripts.js


---

## 💻 How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/Ommali8421/battery-swap-system.git
````

2. **Navigate to the project folder**

```bash
cd battery-swap-system
```

3. **Create and activate virtual environment**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Set up the MySQL database**

* Create a MySQL database named `battery_swap`
* Execute `schema.sql` to create required tables

6. **Add your `.env` file**

```env
SECRET_KEY=your_secret_key
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=battery_swap
DB_PORT=3306
```

7. **Run the Flask App**

```bash
python app.py
