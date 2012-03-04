from django.contrib import admin
from django.contrib.auth.models import User
from donormatch.models import DonorProfile, UserProfile

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class DonorProfileInline(admin.StackedInline):
    model = DonorProfile

class UserProfileAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline, DonorProfileInline]
admin.site.register(User, UserProfileAdmin)
