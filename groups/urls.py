from django.conf.urls import url
from .import views
from django.urls import path,include

app_name='groups'

urlpatterns = [
    path('',views.ListGroupView.as_view(),name="all"),
    path('new/',views.CreateGroupView.as_view(),name="create"),
    path('posts/in/(?P<slug>[-\w]+)',views.SingleGroupView.as_view(),name="single"),
    path('join/(?P<slug>[-\w]+)',views.JoinGroup.as_view(),name="join"),
    path('leave/(?P<slug>[-\w]+)',views.LeaveGroup.as_view(),name="leave"),
    
    
]
