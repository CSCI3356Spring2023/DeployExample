from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserType(models.Model):
    user_type = models.CharField(max_length=100)

    def __unicode__(self):
        return self.user_type

class ContactsModel(models.Model):
    from_email = models.EmailField()
    repeat_email = models.EmailField()
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    subject = models.CharField(max_length=1024)
    message = models.TextField(max_length=1024*2) 
    def __unicode__(self):
        return self.nameclass 

class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

obj1 = UserType(user_type='faculty')
obj1.save()
obj2 = UserType(user_type='student')
obj2.save()


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user',on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default = False)
    website = models.URLField(default='', blank=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    organization = models.CharField(max_length=100, default='', blank=True)


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)