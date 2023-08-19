from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from app.forms import *
from django.core.mail import send_mail
from app.models import *
import  random
from random import randrange
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def Home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        PO=Profile.objects.get(username=UO)
        d={'UO':UO, 'PO':PO,'username':username}
        return render(request, 'Home.html', d)

    return render(request, 'Home.html')

def Registration(request):
    PF=ProfileForm()
    UF=Userform()
    d={'PF':PF,'UF':UF,}
    if request.method == 'POST':
        UFD=Userform(request.POST)
        PFD=ProfileForm(request.POST, request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            account_no=''
            for i in range(10):
                x=random.randrange(0,10)
                account_no+=str(x)
            NUFD=UFD.save(commit=False)
            NUFD.set_password(UFD.cleaned_data['password'])
            NUFD.save()
            NPFD=PFD.save(commit=False)
            NPFD.username=NUFD
            NPFD.account_no=account_no
            NPFD.save()
            send_mail(
                'Registration',  # subject
                f'Registration is successful and your account_number is {account_no}',  # message
                'mgangadhara1627@gmail.com',  # from_email
                [NUFD.email],  # recipient_list
                fail_silently=True)
            return HttpResponse('data is successfully....')
        return HttpResponse('Invalid Data')
    return render(request, 'Registration.html',d)


def User_Login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        AO=authenticate(username=username,password=password)
        if AO and AO.is_active:
            login(request,AO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('Home'))
        else:
            return HttpResponse('User Is In Valid')
            
    return render(request,'User_Login.html')

@login_required 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('User_Login'))
@login_required
def transactions(request):
    if request.method == 'POST':
        UN = request.session.get('username')
        try:
            UO = User.objects.get(username=UN)
            PO, created = Profile.objects.get_or_create(username=UO)
            client = request.POST['mobile']
            money = request.POST['money']
            if PO.balance >= int(money):
                PO.balance -= int(money)
                PO.save()
                CPMD, created = Profile.objects.get_or_create(mobile_no=client)
                CPMD.balance += int(money)
                CPMD.save()
                SD = CPMD.username.username
                SH = History.objects.create(Sender=UN, Reciver=SD, Money=int(money))
                return HttpResponse('Transaction Is Completed')
            else:
                return HttpResponse('Not Enough Balance')
        except User.DoesNotExist:
            return HttpResponse('User does not exist')
        except Profile.DoesNotExist:
            return HttpResponse('Profile does not exist')
    
    return render(request,'transactions.html')

@login_required
def History_display(request):
    UN=request.session.get('usernames')
    HSD=History.objects.filter(Sender=UN)
    HRD=History.objects.filter(Reciver=UN)
    d={'HRD':HSD, 'HRD':HRD}
    return render(request,'History_display.html',d)


@login_required
def Transactions_acc(request):
    if request.method == 'POST':
        UN = request.session.get('username')
        try:
            UO = User.objects.get(username=UN)
            PO, created = Profile.objects.get_or_create(username=UO)
            client = request.POST['acc']
            money = request.POST['money']
            if PO.balance >= int(money):
                PO.balance -= int(money)
                PO.save()
                CPMD, created = Profile.objects.get_or_create(account_no=client)
                CPMD.balance += int(money)
                CPMD.save()
                SD = CPMD.username.username
                SH = History.objects.create(Sender=UN, Reciver=SD, Money=int(money))
                return HttpResponse('Transaction Is Completed')
            else:
                return HttpResponse('Not Enough Balance')
        except User.DoesNotExist:
            return HttpResponse('User does not exist')
        except Profile.DoesNotExist:
            return HttpResponse('Profile does not exist')
    return render(request,'Transactions_acc.html')


def forgot_password(request):
    if request.method == 'POST':
        UN=request.POST.get('username')
        PS=request.POST.get('password')
        LUO=User.objects.filter(username=UN)
        if LUO:
            UO=LUO[0]
            UO.set_password(PS)
            UO.save()
            return HttpResponseRedirect(reverse('User_Login'))
        else:
            return HttpResponse('Invalid Username And Password')
    return render(request,'forgot_password.html')