# from crypt import methods
from http import server
from turtle import home
from flask import Flask, render_template, Blueprint, url_for, request, redirect
from flask_login import login_required, current_user
import smtplib
from email.message import EmailMessage
from Breast_Cancer import input_output

main = Blueprint("doctor_main", __name__)

@main.route('/')
def home():
    return render_template("home_page.html")
@main.route('/about-us') 
def about_us():
    return render_template("about_us.html")  

@main.route('/contact-us',methods=['GET','POST']) 
def contact_us():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        subject=request.form.get('subject')
        message=request.form.get('message')

        msg = EmailMessage()
        msg1='Name: {}\n\nEmail: {}\n\n{}'.format(name,email,message)
        msg.set_content(msg1)

        msg['Subject'] = subject
        msg['From'] = "breast.cancer.prediction.2022@gmail.com"
        msg['To'] = "breastcancerprediction6@gmail.com"

        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("breast.cancer.prediction.2022@gmail.com","@m416#3x")
        server.send_message(msg)
    return render_template("contact_us.html")

@main.route('/prediction',methods=['GET','POST'])
def prediction():
    result=''
    if request.method=='POST':
        radius=request.form.get('radius')
        texture=request.form.get('texture')
        perimeter=request.form.get('perimeter')
        area=request.form.get('area')
        smoothness=request.form.get('smoothness')
        compactness=request.form.get('compactness')
        concavity=request.form.get('concavity')
        c_points=request.form.get('c_points')
        symmetry=request.form.get('symmetry')
        f_dimension=request.form.get('f_dimension')
        output,percentage=input_output.get_values(radius,texture,perimeter,area,smoothness,compactness,concavity,c_points,symmetry,f_dimension)
        if output==1:
            result="\n"+"It is a Malignant Cancer with "+ percentage+"% Accuracy"
        else:
            result="\n"+"It is a Benign Cancer with "+ percentage+"% Accuracy"
    

    return render_template("prediction.html", name=current_user.username, output=result)
    