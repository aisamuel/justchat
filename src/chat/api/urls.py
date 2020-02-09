from django.urls import path, re_path
# from .views import index, room
from .views import (
     ChatListView,
     ChatDetailView,
     ChatCreateView,
     ChatUpdateView,
     ChatDeleteView
)
app_name = 'chat'

urlpatterns = [
    path('', ChatListView.as_view()),
    path('create/', ChatCreateView.as_view()),
    path('<pk>', ChatDetailView.as_view()),
    path('<pk>/update/', ChatUpdateView.as_view()),
    path('<pk>/delete', ChatDeleteView.as_view())
    # path('', index, name='index'),
    # re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]
 