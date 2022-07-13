from ast import For
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from member.models import Member

# Create your views here.


def memberEmailSend(request):
    title = "Member Email Send"
    if request.method == 'POST':
        members = Member.objects.all()
        for member in members:
            subject = request.POST.get('subject', '')
            note = request.POST.get('note', '')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = member.email
            member_data = {
                'name': member.name,
                'email': member.email,
                'password': member.password,
                'website_url': member.website_url,
                'note': note,
            }
            html_content = render_to_string(
                'members/email_template.html', {'member_data': member_data})
            email = EmailMessage(subject,html_content,email_from,[recipient_list])
            email.content_subtype = "html"
            email.send()
        return HttpResponseRedirect('/member/email/send')
    else:
        members = Member.objects.all()
    return render(request, 'members/member_email_send.html', {'title': title})


def memberList(request):
    title = "Member List"
    members = Member.objects.all()
    return render(request, 'members/index.html', {'title': title, 'members': members})
