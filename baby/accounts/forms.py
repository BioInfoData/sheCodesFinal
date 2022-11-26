from .models import Profile, Details, Connection
from django import forms


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('name','email','phone','type','gender','profileimg')

class DetailsForm(forms.ModelForm):

    class Meta:
        model = Details
        fields = ('birth', 'exp')

class ConnectionForm(forms.ModelForm):
    def __init__(self, user_profile, *args, **kwargs): # this to include when want to present only parents/baby
        super(ConnectionForm, self).__init__(*args, **kwargs)
        if user_profile.type == "Parent":
            type = "Babysitter"
        elif user_profile.type == "Babysitter":
            type = "Parent"
        self.fields['connected_user'] = forms.ModelMultipleChoiceField(queryset=Profile.objects.filter(type=type),
                                                                       widget=forms.CheckboxSelectMultiple())


    class Meta:
        model = Connection
        fields = ('connected_user',)