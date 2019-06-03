from django.urls import path, re_path, include

from .views.userviews import UserListView, UserDetailView, GroupListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    re_path('users/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', UserDetailView.as_view(), name='user-detail'),
    #path('users/<email>', UserDetailView.as_view(), name='user-detail'),
    path('groups/', GroupListView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
]
