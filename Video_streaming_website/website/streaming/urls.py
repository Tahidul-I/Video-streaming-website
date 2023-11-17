from django.urls import path
from streaming import views

urlpatterns=[
    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
    path('user_registration/',views.user_registration,name='user_registration'),
    path('watch<int:id>/',views.watch,name='watch'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
]