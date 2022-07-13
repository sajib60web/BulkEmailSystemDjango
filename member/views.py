from urllib import request
from django.shortcuts import render

from member.models import Member

# Create your views here.


def memberList(request):
    title = "Member List"
    members = Member.objects.all()
    return render(request, 'members/index.html', {'title': title, 'members': members})
