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

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView

from ..forms.guest import GuestNameForm
from .models import Room
from .chatroom.chatrooms import views
from .chatroom.chatrooms.utils.auth import get_login_url
class RoomsListView(ListView):
    """View to show the list of rooms available """
    context_object_name = "rooms"
    template_name = "chatroom/chatrooms/templates/rooms_list.html"
    paginate_by = 20

    def get_queryset(self):
        filters = {}
        if self.request.user.is_anonymous():
            filters['allow_anonymous_access'] = True
        return Room.objects.filter(**filters)

class RoomView(DetailView):
    """View for the single room """
    model = Room
    context_object_name = 'room'
    template_name = "chatroom/chatrooms/templates/room.html"

class GuestNameView(FormView):
    """Shows the form to choose a guest name to anonymous users """
    form_class = GuestNameForm
    template_name = 'chatroom/chatrooms/templates/guestname_form.html'

    def get_context_data(self, **kwargs):
        kwargs.update(super(GuestNameView, self).get_context_data(**kwargs))
        room_slug = self.request.GET.get('room_slug')
        next = ''
        if room_slug:
            next = reverse('room_view', kwargs={'slug': room_slug})
        kwargs['login_url'] = get_login_url(next)
        return kwargs

    def get_initial(self):
        init = super(GuestNameView, self).get_initial()
        room_slug = self.request.GET.get('room_slug')
        if room_slug:
            init.update(room_slug=room_slug)
        return init

    def form_valid(self, form):
        guest_name = form.cleaned_data.get('guest_name')
        room_slug = form.cleaned_data.get('room_slug')
        self.request.session['guest_name'] = guest_name
        if room_slug:
            redirect_url = reverse('room_view', kwargs={'slug': room_slug})
        else:
            redirect_url = reverse('rooms_list')
        return HttpResponseRedirect(redirect_url)

@csrf_protect
def messages(request):
    if request.method == 'POST':
            return HttpResponseRedirect('/chatroom/chatrooms/templates/guestname_form.html')
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            message = "New user has requested an account: \n" + "\nemail: " + form.cleaned_data['email'] + "\npassword: " + form.cleaned_data['password1']
            send_mail(
            'New User Request',
            message,
            'dbd62@cornell.edu',
            ['dbd62@cornell.edu'],
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
    'index.html',
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
def navBar(request):
    return render(request,
    'navBar.html',
    )
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
