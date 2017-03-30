from django.contrib import admin
from login.models import *

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(FeeType)
admin.site.register(Payment)
