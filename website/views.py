from os import stat
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
import pyotp
import random
import json
from django.urls import reverse
import datetime

hotp = pyotp.TOTP('base32secret3232', digits=4)

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':

        user_email_id = request.POST['user_email']

        file = open('saving_mail_ids.txt', 'w')
        file.write(user_email_id)
        file.close()

        # stats for geenrating OTP
        otp = hotp.now()
        
        msg_html = render_to_string('otp-email.html', {"otp": otp})

        email = EmailMultiAlternatives(f'Fitlife.ai Account - {otp} is your OTP for secure access', '', settings.EMAIL_HOST_USER, [user_email_id])
        email.attach_alternative(msg_html, "text/html")
        email.send()

        return render(request,'login-next.html', {"user_email_id": user_email_id})

        #return redirect('login_next', user_email_id = user_email_id)

    return render(request,'login.html')

def login_next(request):
    if request.method == 'POST':
        otp1 = request.POST['otp_1']
        otp2 = request.POST['otp_2']
        otp3 = request.POST['otp_3']
        otp4 = request.POST['otp_4']

        user_otp = otp1 + otp2 + otp3 + otp4
        
        status = hotp.verify(str(user_otp))

        if status == True:
            # messages.success(request, "Successfully Logged In")
            # return HttpResponse('<h1>Successfully Logged In</h1>')
            return redirect('dashboard')

        else:
            messages.warning(request, "Invalid OTP! Please try again")
            return redirect('login_next')
        
    return render(request,'login-next.html')

def resend_for_login(request):

    file = open("saving_mail_ids.txt").read()
    #print(file) 
    
    #stats for geenrating OTP
    otp = hotp.now()

    msg_html = render_to_string('otp-email.html', {"otp": otp})

    email = EmailMultiAlternatives(f'Fitlife.ai Account - {otp} is your OTP for secure access', '', settings.EMAIL_HOST_USER, [file])
    email.attach_alternative(msg_html, "text/html")
    email.send()

    return render(request,'login-next.html', {"user_email_id": file})

   
def dashboard(request):
    return render(request,'dashboard.html')

def gender(request):
    # if request.method == 'POST':
    #     gender_1 = request.POST['genderm']
    #     gender_2 = request.POST['genderf']
    #     print(gender_1,gender_2)
        
    #     redirect('index')

    # if gender = Male:
    # redirect to focus_area_male  and active_status_male
    # else:
    # redirect to focus_area_female and active_status_female

    return render(request,'gender.html')

def focus_area_female(request):
    return render(request,'focus-area-female.html')

def focus_area_male(request):
    return render(request,'focus-area-male.html')

def personal_details(request):
    if request.method == 'POST':
        user_name = request.POST['name']
        user_age = request.POST['age']
        user_blood_group = request.POST['bloodgroup']
        
    return render(request,'personal-details.html')

def body_details(request):
    if request.method == 'POST':
        user_height = request.POST['height']
        user_current_weight = request.POST['current-weight']
        user_targeted_weight = request.POST['targeted-weight']
        print(user_height,user_current_weight,user_targeted_weight)

    return render(request,'body-details.html')

def active_status_female(request):
    return render(request,'active-status-female.html')

def active_status_male(request):
    return render(request,'active-status-male.html')

def main_goal(request):
    return render(request,'main-goal.html')



