from django.urls import path
from . import views
urlpatterns = [
    path('member/email/send', views.memberEmailSend, name='member_email_send'),
    path('member/list', views.memberList, name='member_list'),
]
