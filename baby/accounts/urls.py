from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('singup/', views.singup_view, name="singup_form"),
    path('login/', views.login_view, name="login_form"),
    path('logout/',views.logout_view, name = 'logout'),
    path('settings/', views.settings_view, name="settings_form"),
    path('details/', views.babysitter_details, name="details_form"),
    path('connections/', views.connections_view, name="connections_form"),
    path('wellcome/', views.wellcome_view, name='wellcome'),
    path('search/', views.search_view, name='search_form'),
    path('<str:username>/', views.info_view, name='info')
]