from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('editprofile/', views.edit_profile, name='edit_profile'),
    path('new/', views.create, name='create'),
    path('confirmpickup/<int:customer_id>/', views.confirm_pickup, name='confirm_pickup'),
    path('weeklypickupfilter/<str:weekday>/', views.weekly_pickup_filter, name='weekly_pickup_filter'),
    path('weeklypickupfilter/', views.weekly_pickup_filter, name='weekly_pickup_filter')
]