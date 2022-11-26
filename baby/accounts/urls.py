from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('singup/', views.singup_view, name="singup_form"),
    path('settings/', views.settings_view, name="settings_form"),
    path('details/', views.babysitter_details, name="details_form"),
    path('connections/', views.connections_view, name="connections_form"),
    path('wellcome/', views.wellcome_view, name='wellcome'),
    path('<str:username>/', views.feed_view, name='feed')
]