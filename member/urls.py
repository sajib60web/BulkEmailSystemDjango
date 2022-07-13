from django.urls import path
from . import views
urlpatterns = [
    path('member/list', views.memberList, name='member_list'),
]
