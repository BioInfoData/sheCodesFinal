from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import ProfileForm, DetailsForm, ConnectionForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Details, Connection
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



@login_required
def settings_view(request):

    if request.method == 'POST':
        user_profile = Profile.objects.get(user=request.user)
        user_profile.name = request.POST['name']
        user_profile.user = request.user
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
            new_details = Details.objects.create(user=user_model, userid=user_model.id)
            new_details.save()

            return redirect('accounts:details_form')

        elif user_profile.type == "Parent":
            return redirect('accounts:connections_form')
    else:
        #profile_form = ProfileForm(current_user=request.user) # TODO remove this. only example for
        profile_form = ProfileForm()
        return render(request, "accounts/general_settings.html", {'profile_form': profile_form})

@login_required
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

@login_required
def connections_view(request):
    if request.method == 'POST':
        #print(request.user.username)
        print(type(request.POST['connected_user']))
        print(request.POST)
        user_connections = Connection.objects.create(username=request.user.username)
        user_connections.save()
        users_to_add = request.POST.getlist('connected_user')
        print(users_to_add)
        for connected_id in users_to_add:
            connected_profile = Profile.objects.get(id=connected_id)
            print(connected_profile)
            user_connections.connected_user.add(connected_profile)

        return redirect('homepage')
    else:
        user_profile = Profile.objects.get(user=request.user) # use the type info from profile to present only parent/babysitter
        connection_form = ConnectionForm(user_profile=user_profile)
        return render(request, "accounts/connections.html", {'connection_form': connection_form})