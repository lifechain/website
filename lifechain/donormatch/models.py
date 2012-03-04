from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    SEX_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('y', 'Yes, Please')
    )
    user = models.ForeignKey(User)
    birthday = models.DateField()
    sex = models.CharField(max_length=1, choices = SEX_CHOICES)
    location = models.CharField(max_length=255, blank = True)
    lattitude = models.IntegerField(blank = True)
    longitude = models.IntegerField(blank = True)
    phone = models.CharField(max_length=15, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return self.user.username

class DonorProfile(models.Model):
    user = models.ForeignKey(User)
    blood_type = models.CharField(max_length=2, blank = True)
    im1 = models.CharField(max_length=10, blank = True)
    im2 = models.CharField(max_length=10, blank = True)
    im3 = models.CharField(max_length=10, blank = True)
    im4 = models.CharField(max_length=10, blank = True)
    im5 = models.CharField(max_length=10, blank = True)
    im6 = models.CharField(max_length=10, blank = True)
    ethnicity = models.CharField(max_length=10, blank = True)
    smoker = models.BooleanField(blank = True)
    drug_use = models.BooleanField(blank = True)
    medical_conditions = models.TextField(blank = True)
    hla_type = models.CharField(max_length=10, blank = True)
    height = models.IntegerField(blank = True)
    weight = models.IntegerField(blank = True)
    allergies = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return self.user.username

class UserLink(models.Model):
    user_from = models.ForeignKey(User, related_name="user_from")
    user_to = models.ForeignKey(User, related_name="user_to")

    def __unicode__(self):
        return "%s -> %s" % (self.user1.username, self.user2.username)
