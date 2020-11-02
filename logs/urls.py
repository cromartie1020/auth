from django.urls import path
from .views import logs, topics, topic, NewTopicView,edit_entry
 
urlpatterns=[
    path('',logs,name='logs'),
    path('topics/',topics,name='topics'),
    path('topic/<int:id>/',topic,name='topic'),
    path('new_topic',NewTopicView,name='new_topic'),
    path('edit_entry/<int:id>',edit_entry,name='edit_entry'),
    path('edit_entry/<int:id>/save/',edit_entry,name='edit_entry'),
]