from django.shortcuts import render, redirect
import requests
import random

# Create your views here.
def home_page(request):


    if request.method == 'POST':
        get_otp = request.POST['otp']
        if get_otp == request.session['otp']:
            url = "https://www.fast2sms.com/dev/bulkV2"
            params = {
                'authorization': 'EeDjaUaTXwWFefjbi43tnnBHlJF2RC2BX0dx5nsYESHucTWo6xxTME1Nz1Fk',
                'route' : 'q',
                'message' : "Your Acct debited for Rs 50000.00",
                'numbers' : request.session['phone'],
                'flash' : "0" 
            }
            headers = {
                'cache-control': "no-cache"
            }
            response = requests.get(url, params=params)
            print(response.text)
            print('Verified')
            return redirect('prank')
    return render(request, 'index.html')

def send_otp(phone_number, otp):
    url = "https://www.fast2sms.com/dev/bulkV2"
    params = {
        'authorization': 'EeDjaUaTXwWFefjbi43tnnBHlJF2RC2BX0dx5nsYESHucTWo6xxTME1Nz1Fk',
        'route' : 'otp',
        'variables_values' : otp,
        'numbers' : phone_number,
        'flash' : "0" 
    }
    headers = {
        'cache-control': "no-cache"
    }
    response = requests.get(url, params=params)
    print(response.text)

    
def prank(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        request.session['phone'] = phone
        otp = str(random.randint(1000, 9999))
        print(otp)
        send_otp(phone, otp)
        request.session['otp'] = otp
    
    

    
    return render(request, 'ph.html')