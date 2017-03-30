from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import JsonResponse
from django.http import HttpResponse
import json
from login.forms import *
from login.models import *
from time import strftime
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            message = "New user has requested an account: \n" + "\nemail: " + form.cleaned_data['email'] + "\npassword: " + form.cleaned_data['password1']
            send_mail(
            'New User Request',
            message,
            'ss3629@cornell.edu',
            ['ss3629@cornell.edu'],
            fail_silently=False,
            )
            return HttpResponseRedirect('/registration/success.html')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render(request,
    'registration/register.html',
    { 'form': form },
    )
def login(request):
    return render(request,
    'login.html',
    )
@login_required
def home(request):
    return render(
    request,
    'home.html',
    {
        'user': UserProfile.objects.get(user=request.user).first_name
    }
    )

def events(request):
    print (request.user)
    to_return = {}
    to_return['events'] = []
    user_profile = UserProfile.objects.get(user=request.user);
    for event in events:
        l = []
        start_time = event.start_time
        end_time = event.end_time
        while start_time < end_time:
            l.append(start_time)
            start_time += datetime.timedelta(minutes=30)
        time_array = [(t.strftime(" %I%M%p")).replace(' 0',' ') for t in l]
        if event.owner == user_profile:
            to_return['events'].append({'date': event.start_time.strftime("%Y-%m-%d"), 'time_array': time_array, 'show_class': "my_event", 'event_id': event.id })
        else:
            to_return['events'].append({'date': event.start_time.strftime("%Y-%m-%d"), 'time_array': time_array, 'show_class': "event", 'event_id': event.id })
        print (to_return)
    return JsonResponse(to_return)
def base(request):
    return render(request,
    'index.html',
    )
def fypusRequest(request):
    return render(request,
    'fypusRequest.html',
    )
def fypusRequestYou(request):
    return render(request,
    'fypusRequestYou.html',
    )
def home(request):
    return render(request,
    'home.html',
    )
def index(request):
    return render(request,
    'index.html',
    )
def join(request):
    return render(request,
    'join.html',
    )
def joinRequest(request):
    return render(request,
    'joinRequest.html',
    )
def profile(request):
    return render(request,
    'profile.html',
    )
def recruitOthers(request):
    return render(request,
    'recruitOthers.html',
    )
def requestRecieved(request):
    return render(request,
    'requestRecieved.html',
    )
def requestToJoin(request):
    return render(request,
    'requestToJoin.html',
    )
def yourSavings(request):
    return render(request,
    'yourSavings.html',
    )
def Search(request):
    return render(request,
    'Search.html',
    )
def help(request):
    return render(request,
    'help.html',
    )
def Recruit2(request):
    return render(request,
    'Recruit2.html',
    )
def NewLeague(request):
    return render(request,
    'NewLeague.html',
    )
def AddLeague(request):
    return render(request,
    'AddLeague.html',
    )
def messages(request):
    return render(request,
    'messages.html',
    )
def navBar(request):
    return render(request,
    'navBar.html',
    )
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
