from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import ProfileForm, DetailsForm, ConnectionForm, SearchForm, RemoveConnectionForm, ReplyForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Details, Connection, Search, SearchMessage, Reply
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

def singup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('accounts:singup_form')

        elif password != password2:
            messages.info(request, 'Password Not Matching')
            return redirect('accounts:singup_form')
        # TODO password has min numbers/ letters (.is_valid?)
        else:
            user = User.objects.create_user(username=username,  password=password)
            user.save()
            # log user in and redirect to settings page
            user_login = auth.authenticate(username=username, password=password)
            auth.login(request, user_login)

            # create a Profile object for the new user
            user_model = User.objects.get(username=username)
            new_profile = Profile.objects.create(user=user_model, userid = user_model.id)
            new_profile.save()

            #profile_form = ProfileForm()
            return redirect('accounts:settings_form')

    else:
        form = UserCreationForm()
        return render(request, 'accounts/singup.html', {'form': form})



@login_required(login_url='accounts:login_form')
def settings_view(request):

    if request.method == 'POST':
        user_profile = Profile.objects.get(user=request.user)
        user_profile.name = request.POST['name']
        user_profile.user = request.user
        user_profile.username = request.user.username
        user_profile.type = request.POST['type']
        user_profile.gender = request.POST['gender']
        user_profile.phone = request.POST['phone'] #TODO check valid phone

        email = request.POST['email']
         # TODO this is not working. check email mot exists
        user_profile.email = email #TODO check valid email


        if request.POST['profileimg']:
            upload = request.FILES['profileimg']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            user_profile.profileimg = upload


        user_profile.save()

        if user_profile.type == "Babysitter":
            # create a Detail object for the new user
            user_model = User.objects.get(username=request.user)
            new_details = Details.objects.create(user=user_model,
                                                 userid=user_model.id,
                                                 username=user_model.username)
            new_details.save()

            return redirect('accounts:details_form')

        elif user_profile.type == "Parent":
            return redirect('accounts:connections_form')
    else:
        profile_form = ProfileForm()
        return render(request, "accounts/general_settings.html", {'profile_form': profile_form})

@login_required(login_url='accounts:login_form')
def babysitter_details(request):
    if request.method == 'POST':
        user_details = Details.objects.get(user=request.user)
        user_details.exp = request.POST['exp']
        user_details.birth = request.POST['birth']
        user_details.save()
        return redirect('accounts:connections_form')
    else:
        details_form = DetailsForm()
        return render(request, "accounts/babysitter_details.html", {'details_form': details_form})

@login_required(login_url='accounts:login_form')
def remove_connections_view(request):
    if request.method == 'POST':
        user_connections = get_connections(request.user.username)
        users_to_remove = request.POST.getlist('connected_user')
        for connected_id in users_to_remove:
            connected_profile = Profile.objects.get(id=connected_id)
            user_connections.connected_user.remove(connected_profile)
            # remove the connected user connections
            connected_connections = get_connections(connected_profile.username)
            user_profile = Profile.objects.get(username=request.user.username)
            connected_connections.connected_user.remove(user_profile)
        return redirect('accounts:wellcome')
    else:
        user_profile = Profile.objects.get(user=request.user)
        remove_connection_form = RemoveConnectionForm(user_profile=user_profile)
        return render(request, "accounts/remove.html", {'remove_connection_form': remove_connection_form})

def get_connections(username):
        try:
            user_connections = Connection.objects.get(username=username)
        except Connection.DoesNotExist:
            user_connections = Connection.objects.create(username=username)
            user_connections.save()
        return user_connections

@login_required(login_url='accounts:login_form')
def connections_view(request):
    if request.method == 'POST':
        user_connections = get_connections(request.user.username)
        users_to_add = request.POST.getlist('connected_user')
        for connected_id in users_to_add:
            connected_profile = Profile.objects.get(id=connected_id)
            user_connections.connected_user.add(connected_profile) # add to current user connections
            # add to the connected user connections
            connected_connections = get_connections(connected_profile.username)
            user_profile = Profile.objects.get(username=request.user.username)
            connected_connections.connected_user.add(user_profile)

        return redirect('accounts:wellcome')
    else:
        user_profile = Profile.objects.get(user=request.user) # use the type info from profile to present only parent/babysitter
        connection_form = ConnectionForm(user_profile=user_profile)
        return render(request, "accounts/connections.html", {'connection_form': connection_form})

@login_required(login_url='accounts:login_form')
def info_view(request, username):
    user = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user)
    print(request.path.strip("/"))
    if user_profile.type == "Babysitter":
        bs_details = Details.objects.get(user=user)
        return render(request, 'accounts/info.html', {'user_profile' : user_profile,
                                                      'user_data' : user,
                                                      'bs_details' : bs_details})
    else:
        return render(request, 'accounts/info.html', {'user_profile': user_profile,
                                                      'user_data': user})

@login_required(login_url='accounts:login_form')
def wellcome_view(request):
    user_profile = Profile.objects.get(user=request.user)
    list_connected = []
    try:
        user_connections = Connection.objects.get(username=request.user.username)
        connected = user_connections.connected_user.all()
        for con in connected:
            list_connected.append(con.user.username)
    except Connection.DoesNotExist:
        pass

    return render(request, 'accounts/wellcome.html', {'list_connected' : list_connected,
                                                      'user_profile' : user_profile})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('accounts:wellcome')
        else:
            messages.info(request, 'username or password are incorrect')
            return redirect('accounts:login_form')
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('homepage')


@login_required(login_url='accounts:login_form')
def feed_view(request):

    if request.method == "POST":
        reply = Reply.objects.create(babysitter = request.user.username,
                            message = request.POST['message'])
        search_mes = SearchMessage.objects.get(search=request.POST['search'],
                                  babysitter = request.user.username)
        search_mes.message= request.POST['message']
        search_mes.save()

        current_search = Search.objects.get(id=request.POST['search'])
        current_search.reply.add(reply)
        current_search.save()

        return redirect("accounts:feed")

    else:
        profile = Profile.objects.get(username=request.user.username)
        if profile.type == "Parent":
            parent_search = Search.objects.all().filter(username=request.user.username)
            # TODO order by search id
            return render(request, "accounts/feed.html",
                          {"parent_search": parent_search,
                           "type" : "Parent"})
        else:
            reply_message = SearchMessage.objects.filter(babysitter=request.user.username)
            id_search = reply_message.values_list('search', flat=True)
            parent_search = Search.objects.all().filter(id__in=id_search) # TODO order by search id
            reply_form = ReplyForm(parent_search=parent_search)
            return render(request, "accounts/feed.html",
                          {"parent_search": parent_search,
                           "reply_form" : reply_form,
                           "type" : "Babysitter"})



@login_required(login_url='accounts:login_form')
def search_res_view(request):
    list_selected = request.session['list_selected']  # This was stored in the request in search view
    number_found = len(list_selected)
    return render(request, "accounts/search_results.html",
                  {'list_selected': list_selected,
                   'number_found' : number_found})

@login_required(login_url='accounts:login_form')
def search_view(request):
    if request.method == 'POST':
        list_selected = []

        try: # first get all connection of the user
            user_connections = Connection.objects.get(username=request.user.username)
        except Details.DoesNotExist:
            return redirect('accounts:search_form')

        try: # second - get the connection with the gender
            connected = user_connections.connected_user.filter(gender= request.POST['gender'])
            list_connected = []
            for con in connected:
                list_connected.append(con.user.username)
        except Details.DoesNotExist:
            return redirect('accounts:search_form')

        # third - get the details of the selected babysitters and filter exp
        try:
            selected = Details.objects.filter(username__in=list_connected,
                                                  exp__gte=int(request.POST['min_exp']))

            for sel in selected:
                list_selected.append(sel.username)

            if len(list_selected) > 0: # if found matches
                # 1. create search object
                search = Search.objects.create(username=request.user.username,
                                               gender=request.POST['gender'],
                                               min_exp=int(request.POST['min_exp']),
                                               message = request.POST['message'])
                search.save()
                search.results.set(selected)

                # 2. create parent to babysitter message object
                for babysitter_username in list_selected:
                    reply_message = SearchMessage.objects.create(search = search,
                                                                  parent = request.user.username,
                                                                  message = "",
                                                                  babysitter = babysitter_username)


        except Details.DoesNotExist:
            return redirect('accounts:search_form')

        # case found a relevant connection
        request.session['list_selected'] = list_selected # store in the request to set search res view
        return redirect('accounts:search_res')


    else:
        search_form = SearchForm()
        return render(request, "accounts/search.html", {'search_form': search_form})
