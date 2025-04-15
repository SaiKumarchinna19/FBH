from django.shortcuts import render,redirect,HttpResponse
from .models import Account
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import random

# Create your views here.
def create(request):

    return render(request,'index.html')
def profile(request):
    if request.method=='POST':
        name=request.POST['name']
        dob=request.POST['dob']
        aadhar=request.POST['aadhar']
        phone=request.POST['phone']
        address=request.POST['address']
        email=request.POST['email']
        print(name,dob,aadhar,phone,address,email)
        Account.objects.create(name=name,DOB=dob,Aadhar=aadhar,mobile=phone,address=address,email=email)
        print("successful")
        send_mail(f"hello {name} thank you for creating an account in Our Bank", #subject 
        "FBH fraud Bank of Hyderabad,\n Wel comr to Our Family Of Our Bank \n, we are happy for it \n ,regards \n Mannager(DJD-E1)\n Thank You ****!" #body
        ,settings.EMAIL_HOST_USER,[email],fail_silently=False)
        print(" Sent Successfully")
        messages.success(request,"Successfully Account has been Created...🎉🎉🎉")
    return render(request,'profile.html')
def pin(request):
    if request.method =='POST':
        otp=random.randint(100000,999999)
        acc=request.POST.get('acc')
        data=Account.objects.get(acc=acc)
        email=data.email
        # print(email)
        send_mail(f"hello {data.name}",
        f"FBH Bank of hyd \n the OTP is  {otp} \n Please share otp only with our employees not with the others scammers , it  is kind request \n regards \n manager(DJD -E1) \n we scam because we care"  ,
        settings.EMAIL_HOST_USER,[email],fail_silently=False,
        )
        print("sent successfully")
        data.OTP=otp
        data.save()
        return redirect("valid_otp")

    return render(request,'pin.html')
def valid_otp(request):
    if request.method=='POST':
        acc=request.POST['acc']
        otp=int(request.POST['otp'])
        pin1=int(request.POST['pin1'])
        pin2=int(request.POST['pin2'])
        if pin1 == pin2:
            data =Account.objects.get(acc=acc)
            if data.OTP ==otp:
                data.pin=pin2
                data.save()
                send_mail(f"Hello {data.name}  for Account Number:- {data.acc} -PIN GENERATION",
                          f"FBH Fraud Bank Of Hyderabad (FBH) \n We are happy to scam you \n you Successfully Generated pin , we are happy to inform that we know your otp and pin as well so we are  happy to use your money ('your money is our money our money is our money),\n regards \n manager (DJD-E1) \n we scam because we care ",
                settings.EMAIL_HOST_USER,[data.email],fail_silently=False)
                print("successfully sent ")
            else:
                return HttpResponse("otp missmatched please check again  ")
        else:
            return HttpResponse("****** is not a valid OTP check once again")
    return render(request,'valid_otp.html')
def deposite (request):
    if request.method == "POST":
        acc = int(request.POST['acc'])
        pin = int(request.POST['pin'])
        amount = int(request.POST['balance'])
        try:
            data = Account.objects.get( acc = acc )
        except:
            print("account number is not found")
        if data.pin ==int(pin):
            if amount>=100 :
                data.balance+=amount
                data.save()
                send_mail(f"Dear Customer {data.name} ",
                    f"FBH fraud bank of hyd .{amount}rs/- credited in Your account.\n And your current Balance is {data.balance},Regards \n Manager(DJD-E1)\n Thank You ****! We Scam Because We Care " #body
                    ,settings.EMAIL_HOST_USER,[data.email],fail_silently = False)
                print('sent success')
                return redirect("create")
            else:
                return HttpResponse("enter the valid amount")
        else:
            return HttpResponse("wrong  pin...")
    return render(request,'deposite.html')
def bal(request):
    msg=""
    bal=0
    data=None
    f=False
    if request.method=='POST':
        acc=request.POST.get('acc')
        pin=request.POST.get('pin')
        try:
            data=Account.objects.get(acc=int(acc))
        except:
            # msg="please enter the valid account number"
            pass
        if data is not None:
            if data.pin ==int(pin):
                bal =data.balance
                f=True
            else:
                msg='please enter the valid pin'
        else:
            msg="please enter the valid ccount number"
    context ={
        'bal':bal,
        'var':f,
        'msg':msg
    }
    return render(request,'bal.html',context)
def withdraw(request):
    if request.method == "POST":
        acc = int(request.POST['acc'])
        pin = int(request.POST['pin'])
        amount = int(request.POST['balance'])
        try:
            data = Account.objects.get( acc = acc )
        except:
            print("account number is not found")
        if data.pin ==int(pin):
            if data.balance>=amount and amount>0:
                data.balance-=amount
                data.save()
                send_mail(f"Dear Customer {data.name} ",
                    f"FBH fraud bank of hyd .{amount}rs/- debited in Your account.\n And your current Balance is {data.balance},Regards \n Manager(DJD-E1)\n Thank You ****! We Scam Because We Care " #body
                    ,settings.EMAIL_HOST_USER,[data.email],fail_silently = False)
                print('sent success')
                return redirect("create")
            else:
                return HttpResponse("Insufficient balance")
        else:
            return HttpResponse("wrong  pin...")
    return render(request,'withdraw.html')

# For Transfor the amount from one account number to another account number  ###
def transfer(request):
    msg=""
    if request.method=='POST':
        sender=request.POST.get('sender')
        receiver=request.POST.get('receiver')
        pin=request.POST.get('pin')
        amount=request.POST.get('amount')
        try:
            from_acc=Account.objects.get(acc=sender)
        except:
            msg="Sender account is not valid"
        try:
            to_acc=Account.objects.get(acc=receiver)
        except:
            msg="Receiver account number is not valid"
        if from_acc.pin==int(pin):
            if int(amount)>100 and int(amount)<=1000000 and int (amount) <=from_acc.balance:
                from_acc.balance-=int(amount)
                from_acc.save()
                send_mail(f"Hello {from_acc.name} Account Transfer ",
                          f" FBH Fraud Bank of Hyderbad ,\n from your {from_acc.acc} \n {amount}  has been credited from",
                           f" {from_acc.acc}  and balance is : {to_acc.balance} \n Regrads \n Manager-(DJD-E1) \n We are scam bacause we care ",
                          settings.EMAIL_HOST_USER,[to_acc.email],fail_silently=False)
                print('successfully sent')
            else:
                msg='enter the valid amount'
        else:
            msg='incorrect pin'
    return render(request,'transfer.html',{'msg':msg})