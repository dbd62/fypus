from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

from time import strftime

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    first_name = models.CharField(blank=True, max_length=100)
    last_name = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=15)
    balance = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class FeeType(models.Model):
	fee_type = models.CharField(blank=True, max_length=15)
	amount = models.IntegerField()

class Pending(models.Model):
    name = models.CharField(blank=True, max_length=100)
    business_email = models.CharField(blank=True, max_length=100)
    business_company = models.CharField(blank=True, max_length=100)
    password = models.CharField(blank=True, max_length=100)

class User(models.Model):
    name = models.CharField(blank=True, max_length=100)
    business_email = models.CharField(blank=True, max_length=100)
    business_company = models.CharField(blank=True, max_length=100)
    password = models.CharField(blank=True, max_length=100)
    leagues = models.CharField(blank=True, max_length=100)

class Payment(models.Model):
	user = models.OneToOneField(UserProfile)
	amount = models.IntegerField()
	date = models.DateField(auto_now_add=True)
	fee_type = models.OneToOneField(FeeType)

	def __unicode__(self):
		return str(self.start_time.strftime("%Y-%m-%d %H:%M:%S"))
