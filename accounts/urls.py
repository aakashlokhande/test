from django.urls import path
from . import views
from .views import UserPostListView

urlpatterns = [
    path('register',views.register,name='register'),
    path('profile_view',UserPostListView.as_view(), name='profile_view'),
    path('profile',views.profile,name='profile'),
    path('update',views.update, name='update')
]
