from .models import Profile, Details, Connection, Search, ReplySearch
from django import forms
from django.db.models import Q



class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('name','email','phone','type','gender','profileimg')

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ('birth', 'exp')

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('min_exp', 'gender', 'message')


class ReplyForm(forms.ModelForm):
    def __init__(self, parent_search, *args, **kwargs):
        super(ReplyForm, self).__init__(*args, **kwargs)
        self.fields['search'] = forms.ModelChoiceField(queryset=parent_search)

    class Meta:
        model = ReplySearch
        fields = ('search', 'message')

class ConnectionForm(forms.ModelForm):
    def __init__(self, user_profile, *args, **kwargs): # this to include when want to present only parents/baby
        super(ConnectionForm, self).__init__(*args, **kwargs)
        if user_profile.type == "Parent":
            type = "Babysitter"
        elif user_profile.type == "Babysitter":
            type = "Parent"

        list_connected = []
        try:
            user_connections = Connection.objects.get(username=user_profile.username)
            connected = user_connections.connected_user.all()
            for con in connected:
                list_connected.append(con.user.username)
        except Connection.DoesNotExist:
            pass
        queryset = Profile.objects.filter(type=type).filter(~Q(username__in=list_connected))

        self.fields['connected_user'] = forms.ModelMultipleChoiceField(queryset = queryset,
                                                                       widget=forms.CheckboxSelectMultiple())


    class Meta:
        model = Connection
        fields = ('connected_user',)


class RemoveConnectionForm(forms.ModelForm):
    def __init__(self, user_profile, *args, **kwargs): # this to include when want to present only parents/baby
        super(RemoveConnectionForm, self).__init__(*args, **kwargs)
        list_connected = []
        try:
            user_connections = Connection.objects.get(username=user_profile.username)
            connected = user_connections.connected_user.all()
            for con in connected:
                list_connected.append(con.user.username)
        except Connection.DoesNotExist:
            pass
        queryset = Profile.objects.filter(username__in=list_connected)

        self.fields['connected_user'] = forms.ModelMultipleChoiceField(queryset = queryset,
                                                                       widget=forms.CheckboxSelectMultiple())


    class Meta:
        model = Connection
        fields = ('connected_user',)
