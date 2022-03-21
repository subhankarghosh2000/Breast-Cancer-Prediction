from flask import Flask, Blueprint, render_template, url_for, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
# from validate_email import validate_email
from .models import Doctor
from . import db

auth = Blueprint("auth", __name__)

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        # is_valid = validate_email(email_address=email, check_format=True, check_blacklist=True, check_dns=True, check_smtp=False, smtp_debug=False)
        pwd = request.form.get('password')
        cpwd = request.form.get('cpassword')
        if len(pwd)<8:
            return render_template("sign_up.html", password=True)
        if pwd!=cpwd:
            return render_template("sign_up.html", mismatch=True)
        doctor = Doctor.query.filter_by(email=email).first()
        if doctor:
            return render_template("sign_up.html", alert=True)
        # elif not is_valid:
        #     return render_template("signup.html", unsafe=True)

        new_doctor = Doctor(username=name, email=email, password=generate_password_hash(pwd, method="sha256"))
        db.session.add(new_doctor)
        db.session.commit()

        return redirect(url_for('auth.login'))
    
    return render_template("sign_up.html")

@auth.route('/log-in', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        pwd = request.form.get('password')
        remember = True if request.form.get('remember') else False
        doctor = Doctor.query.filter_by(username=name).first()
        if not doctor:
            return render_template("log_in.html", email_not_exist=True, wrong_pwd=False)
        elif not check_password_hash(doctor.password, pwd):
            return render_template("log_in.html", email_not_exist=False, wrong_pwd=True)

        login_user(doctor, remember=remember)
        return redirect(url_for('doctor_main.prediction'))

    return render_template("log_in.html", email_not_exist=False, wrong_pwd=False)

@auth.route('/log-out')
@login_required
def logout():
    logout_user()
    return redirect(url_for('doctor_main.home'))