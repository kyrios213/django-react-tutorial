from django.urls import path

from . import views

urlpatterns = [
    path('room/', views.RoomView.as_view(), name='room'),
    path('create-room/', views.CreateRoomView.as_view(), name='create-room'),
    path('get-room', views.GetRoomView.as_view(), name='get-room'),
    path('join-room', views.JoinRoomView.as_view(), name='join-room'),
    path('user-in-room', views.UserInRoomView.as_view(), name='user-in-room'),
    path('leave-room/', views.LeaveRoomView.as_view(), name='leave-room'),
]
