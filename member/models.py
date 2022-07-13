import email
from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    website_url = models.CharField(max_length=50)
    join_date = models.DateField()

    class Meta:
        db_table = "members"
