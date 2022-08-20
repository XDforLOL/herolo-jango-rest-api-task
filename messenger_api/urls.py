from django.urls import path
from . import views

urlpatterns = [
    path('send_message/', views.create_message_view, name='send_message'),
    path('read_message=<int:pk>/', views.read_message_view, name='read_message'),
    path('delete_message=<int:pk>/', views.message_delete_view, name='delete_message'),
    path('all_unread/', views.unread_list_messages_view, name='all_unread'),
    path('all_messages/', views.list_all_messages_view, name='all_messages')
]
