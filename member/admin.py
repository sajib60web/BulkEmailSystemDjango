from django.contrib import admin

# Register your models here.
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password', 'website_url', 'join_date']


admin.site.register(Member, MemberAdmin)
