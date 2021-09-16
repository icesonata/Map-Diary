from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    profile_url = models.URLField(max_length=500,
        default='https://www.baytekent.com/wp-content/uploads/2016/12/facebook-default-no-profile-pic1.jpg',
    )

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save()

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(
            user=instance,
            firstname=instance.first_name,
            lastname=instance.last_name,
        )

post_save.connect(create_user_profile, sender=User)
