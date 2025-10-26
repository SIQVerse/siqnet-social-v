from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('', views.inbox_view, name='inbox'),
    path('thread/<int:thread_id>/', views.thread_view, name='thread'),
    path('send/', views.send_message_view, name='send_message'),
]
