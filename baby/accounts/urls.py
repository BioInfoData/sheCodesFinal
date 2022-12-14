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
    path('remove/', views.remove_connections_view, name="remove_connections_form"),
    path('wellcome/', views.wellcome_view, name='wellcome'),
    path('search/', views.search_view, name='search_form'),
    path('search_res/', views.search_res_view, name='search_res'),
    path('feed/', views.feed_view, name='feed'),
    path('<str:username>/', views.info_view, name='info')
]